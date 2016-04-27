# -*- coding: utf-8 -

import MeCab
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.grid_search import GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer

# 参考サイトのコピペ
# 文章をmecabで分かちがきして、名詞・動詞・形容詞の単語一覧を返す
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

# テキスト内の単語の出現頻度を数えて、結果を素性ベクトル化する(Bag of words)
count_vectorizer = CountVectorizer()
feature_vectors = count_vectorizer.fit_transform(wakatis)  # csr_matrix(疎行列)が返る
print 'word数: ' + len(feature_vectors.toarray()[0])

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

# 特徴語の出現頻度を表す素性ベクトル。テキスト件数x特徴語数 サイズのベクトルになる
#  print feature_vectors.toarray()
# [[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0
#   0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
#  [0 0 1 1 0 0 0 0 0 0 1 0 0 0 2 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 2 0
#   0 1 1 0 0 0 0 1 0 0 1 0 1 1 0 0 0 1 0 0 0 1 0]
#  [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
#   0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0]
#  [0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
#   0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0]
# ...

# 素性ベクトルに対応する単語の一覧を取得する
vocabulary = count_vectorizer.get_feature_names()
