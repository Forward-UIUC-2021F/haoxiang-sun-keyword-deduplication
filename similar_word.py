import gensim
from get_embedding import get_embedding
import numpy as np
from numpy.linalg import norm
import traceback


def similar_word(word1, word2, word2vec):

    common, subwords1, subwords2, factor1, factor2 = get_subwords(word1, word2, word2vec)

    embedding1 = np.array([1e-5] * 100)
    embedding2 = np.array([1e-5] * 100)

    threshold = 0.81

    quantity1, quantity2 = 1, 1
    for i in range(len(subwords1)):
        sub = subwords1[i]
        fac = factor1[i]
        try:
            vector = get_embedding(sub, word2vec)
            embedding1 += fac * vector
            quantity1 += 1
        except:
            continue
    embedding1 /= quantity1

    for i in range(len(subwords2)):
        sub = subwords2[i]
        fac = factor2[i]
        try:
            vector = get_embedding(sub, word2vec)
            embedding2 += fac * vector
            quantity2 += 1
        except:
            continue
    embedding2 /= quantity2
    cosine = np.dot(embedding1, embedding2) / (norm(embedding1) * norm(embedding2))
    # print(common)
    # print(subwords1)
    # print(subwords2)
    # print(word1, word2, cosine)
    if cosine >= threshold:
        return True
    return False


def get_subwords(word1, word2, word2vec):
    words1 = word1.split("_")
    words2 = word2.split("_")
    common = list(set(words1) & set(words2))
    ret1, fac1 = [], []
    ret2, fac2 = [], []
    for word in words1:
        if word in common:
            ret1.append(word)
            fac1.append(1.8)
            continue
        try:
            ret1.extend([pair[0] for pair in word2vec.most_similar(word)])
            fac1.extend([pair[1] for pair in word2vec.most_similar(word)])
        except:
            ret1.append(word)
            fac1.append(1)
    for word in words2:
        if word in common:
            ret2.append(word)
            fac2.append(1.8)
            continue
        try:
            ret2.extend([pair[0] for pair in word2vec.most_similar(word)])
            fac2.extend([pair[1] for pair in word2vec.most_similar(word)])
        except:
            ret2.append(word)
            fac2.append(1)
    return common, ret1, ret2, fac1, fac2


# word2vec = gensim.models.Word2Vec.load('./word2vec/word2vec.model').wv
# print(similar_word("data_mining", "data_visualization", word2vec))
# print(similar_word("methods", "strategy", word2vec))
# print(similar_word("techniques", "strategies", word2vec))
