import gensim


def get_embedding(query, word2vec):
    return word2vec[query]
    # word2vecf = gensim.models.KeyedVectors.load_word2vec_format('./word2vecf/word2vecf.model', binary=True)
    #
    # print('Input:{}'.format(query))
    # print()
    # print('-----Result of word2vec')
    # print(word2vec[query])
    # print()
    # print('-----Result of word2vecf')
    # print(word2vecf[query])

word2vec = gensim.models.Word2Vec.load('./word2vec/word2vec.model').wv
# print(get_embedding("semi_supervised", word2vec))
# print(get_embedding("supervised", word2vec))