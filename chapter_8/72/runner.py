# -*- coding: utf-8 -
from stop_word import StopWord
from nltk import stem

stop_word = StopWord()
# print stop_word.exists("is")
# print stop_word.exists("hoge")

def filtered_sentiment():
    lemmatizer = stem.WordNetLemmatizer()

    lines = []
    for line in open('sentiment.txt', 'r'):
        words = line.split(' ')
        fileterd_words = []
        for word in words:
            if not stop_word.exists(word):
                feature = lemmatizer.lemmatize(word)
                fileterd_words.append(feature)
        lines.append(fileterd_words)
    return lines

lines = filtered_sentiment()
print lines
