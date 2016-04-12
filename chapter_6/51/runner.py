# -*- coding: utf-8 -
# (. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．
import re

# パターンの最初にrを付けると、バックスラッシュ文字をそのままバックスラッシュとして扱えるようになる
# ?Pは名前付きグループにする構文
punt = re.compile(r"(?P<punt>[\.:;!\?]) (?P<head>[A-Z])")
sentences = []

for line in open('nlp.txt', 'r'):
    l = line.strip()
    if not l: continue

    # \g<name>は名前付きグループの置換
    sentences.append(punt.sub(r"\g<punt>\n\g<head>", l))

# 51. 空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．
for line in sentences:
    words = line.split(' ')
    for word in words:
        print word
    print ''
