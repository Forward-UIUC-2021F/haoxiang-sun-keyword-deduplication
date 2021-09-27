from sematch.semantic.similarity import WordNetSimilarity
from nltk.stem import PorterStemmer

wns = WordNetSimilarity()
print(wns.word_similarity("computer", "laptop", 'li'))

ps = PorterStemmer()
print(ps.stem("civilization"))