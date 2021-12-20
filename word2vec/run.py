import sys
import gensim

if __name__ == "__main__":
    query = sys.argv[1]
    
    word2vec = gensim.models.Word2Vec.load('./word2vec.model')
    for k, v in word2vec.wv.most_similar(query):
        print(k, v)
