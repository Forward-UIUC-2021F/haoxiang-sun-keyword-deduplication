import sys

sys.path.insert(1, 'C:/Users/ThinkPad/Desktop/keyword_deduplication')
model_dir = '../models/word2vec'
from nltk.stem import PorterStemmer
from keywordsforward.model.word2vec.modeling import Word2vecInferencer
from get_embedding import get_embedding
from similar_word import similar_word
import gensim


def dedup_by_stemming(keywords_list):
    ps = PorterStemmer()
    ret = [keywords_list[0]]
    for i in range(1, len(keywords_list)):
        to_insert = True
        for j in range(len(ret)):
            if ps.stem(keywords_list[i]) == ps.stem(ret[j]):
                to_insert = False
                break
        if to_insert:
            ret.append(keywords_list[i])
    return ret


def word2vec_format(phrase):
    words = phrase.split()
    ret = ""
    for i in words:
        subwords = i.split('-')
        for s in subwords:
            ret += s.lower()
            ret += "_"
    return ret[:-1]


def word2vec_unformat(word):
    words = word.split("_")
    return " ".join(words)


def dedup_by_embedding(keywords_list):
    word2vec = gensim.models.Word2Vec.load('./word2vec/word2vec.model').wv
    formatted_keywords = [word2vec_format(w) for w in keywords_list]
    ret = [formatted_keywords[0]]
    for i in formatted_keywords[1:]:
        to_insert = True
        for j in ret:
            if similar_word(j, i, word2vec):
                to_insert = False
                break
        if to_insert:
            ret.append(i)

    return list(map(word2vec_unformat, ret))

