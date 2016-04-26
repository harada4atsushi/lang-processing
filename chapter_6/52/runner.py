# -*- coding: utf-8 -
from word_splitter import WordSplitter
from stemming.porter2 import stem

word_splitter = WordSplitter('nlp.txt')

for word in word_splitter.words:
    print(word + "\t" + stem(word))
