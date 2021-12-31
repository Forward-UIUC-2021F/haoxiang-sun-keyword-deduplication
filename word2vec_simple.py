import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()
import numpy as np
import pandas as pd
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords


def remove_stop_words(corpus):
    stop_words = stopwords.words('english')
    results = []
    for text in corpus:
        tmp = text.split(' ')
        tmp = [w.lower() for w in tmp]
        for stop_word in stop_words:
            if stop_word in tmp:
                tmp.remove(stop_word)
        results.append(" ".join(tmp))
    return results


def vec_distance(vec1, vec2):
    ret = 0
    for idx in range(len(vec1)):
        ret += (vec1[idx] - vec2[idx]) ** 2
    return round(ret ** 0.5, 3)


# function to convert numbers to one hot vectors
def to_one_hot_encoding(data_point_index):
    one_hot_encoding = np.zeros(ONE_HOT_DIM)
    one_hot_encoding[data_point_index] = 1
    return one_hot_encoding


corpus = ['A database is an organized collection of structured information',
          'Most databases use SQL for writing and querying data',
          'A distributed database consists of two or more files located in different sites',
          'Hierarchical database can be accessed and updated rapidly',
          'A network databases are mainly used on a large digital computers',
          'Machine learning is seen as part of the artificial intelligence',
          'Supervised learning requires training data to be totally labeled',
          'Data mining is related field focusing on exploratory data analysis',
          'Learning algorithms work on the basis of strategies, algorithms',
          'Labeling can be used to improve the algorithms for determining correct answers']

corpus = remove_stop_words(corpus)
words = []
for text in corpus:
    sentence = text.split(' ')
    for word in sentence:
        words.append(word.lower())
    for i in range(len(sentence) - 1):
        words.append(sentence[i].lower() + " " + sentence[i + 1].lower())

words = set(words)
words = list(words)
WINDOW_SIZE = 3
ONE_HOT_DIM = len(words)
EMBEDDING_DIM = 3

word2int = {}
for i, word in enumerate(words):
    word2int[word] = i

sentences = []
for sentence in corpus:
    sentences.append(sentence.split())

data = []
for sentence in sentences:
    for idx, word in enumerate(sentence):
        for neighbor in sentence[max(idx - WINDOW_SIZE, 0): min(idx + WINDOW_SIZE, len(sentence)) + 1]:
            if neighbor != word:
                data.append([word, neighbor])

df = pd.DataFrame(data, columns=['input', 'label'])

X = []  # input word
Y = []  # target word

for x, y in zip(df['input'], df['label']):
    X.append(to_one_hot_encoding(word2int[x]))
    Y.append(to_one_hot_encoding(word2int[y]))

# convert them to numpy arrays
X_train = np.asarray(X)
Y_train = np.asarray(Y)

# making placeholders for X_train and Y_train
x = tf.placeholder(tf.float32, shape=(None, ONE_HOT_DIM))
y_label = tf.placeholder(tf.float32, shape=(None, ONE_HOT_DIM))

# hidden layer: which represents word vector eventually
W1 = tf.Variable(tf.random_normal([ONE_HOT_DIM, EMBEDDING_DIM]))
b1 = tf.Variable(tf.random_normal([1]))  # bias
hidden_layer = tf.add(tf.matmul(x, W1), b1)

# output layer
W2 = tf.Variable(tf.random_normal([EMBEDDING_DIM, ONE_HOT_DIM]))
b2 = tf.Variable(tf.random_normal([1]))
prediction = tf.nn.softmax(tf.add(tf.matmul(hidden_layer, W2), b2))

# loss function: cross entropy
loss = tf.reduce_mean(-tf.reduce_sum(y_label * tf.log(prediction), axis=[1]))

# training operation
train_op = tf.train.GradientDescentOptimizer(0.05).minimize(loss)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

iteration = 10001
for i in range(iteration):
    # input is X_train which is one hot encoded word
    # label is Y_train which is one hot encoded neighbor word
    sess.run(train_op, feed_dict={x: X_train, y_label: Y_train})
    if i % 2000 == 0:
        print('iteration ' + str(i) + ' loss is : ', sess.run(loss, feed_dict={x: X_train, y_label: Y_train}))

# Now the hidden layer (W1 + b1) is actually the word look up table
vectors = sess.run(W1 + b1)
x1 = [v[0] for v in vectors]
x2 = [v[1] for v in vectors]
x3 = [v[2] for v in vectors]

w2v_df = pd.DataFrame({'x1': x1, 'x2': x2, 'x3': x3})
w2v_df.insert(0, "word", words)
print(w2v_df)
print(vec_distance(vectors[word2int['database']], vectors[word2int['hierarchical database']]))
print(vec_distance(vectors[word2int['database']], vectors[word2int['hierarchical']]))
print(vec_distance(vectors[word2int['algorithms']], vectors[word2int['computers']]))
print(vec_distance(vectors[word2int['algorithms']], vectors[word2int['learning']]))
