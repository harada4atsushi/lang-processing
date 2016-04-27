# -*- coding: utf-8 -

# 参考URL
# https://datumstudio.jp/backstage/662
# http://qiita.com/quvo/items/1f4075203854ced19ec5
# http://blog.livedoor.jp/riku_kanzaki/archives/2014-10.html

import MeCab
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.grid_search import GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer

def wakati(text):
    tagger = MeCab.Tagger()
    #text = text.encode("utf-8")
    node = tagger.parseToNode(text)
    word_list = []
    while node:
        pos = node.feature.split(",")[0]
        if pos in ["名詞", "動詞", "形容詞"]:
            lemma = node.feature.split(",")[6].decode("utf-8")
            if lemma == u"*":
                lemma = node.surface.decode("utf-8")
            word_list.append(lemma)
        node = node.next
    return u" ".join(word_list[1:-1])


def parse():
    lines = []
    for line in open('data.tsv', 'r'):
        arr = line.split("\t")
        lines.append(arr)
    return lines

wakatis = []
for line in parse():
  wakatis.append(wakati(line[0]))

# テキスト内の単語の出現頻度を数えて、結果をベクトル化する
count_vectorizer = CountVectorizer()
feature_vectors = count_vectorizer.fit_transform(wakatis)  # csr_matrix(疎行列)が返る

# print feature_vectors
  # (0, 24)       1
  # (0, 42)       1
  # (1, 58)       1
  # (1, 2)        1
  # (1, 38)       1
  # (1, 35)       2
  # (1, 54)       1
  # (1, 47)       1
  # (1, 22)       1
  # (1, 50)       1
  # (1, 44)       1
  # (1, 14)       2
  # ...

vocabulary = count_vectorizer.get_feature_names()
print vocabulary
