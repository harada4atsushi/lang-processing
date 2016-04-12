# -*- coding: utf-8 -
# (. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．
import re

# パターンの最初にrを付けると、バックスラッシュ文字をそのままバックスラッシュとして扱えるようになる
# ?Pは名前付きグループにする構文
punt = re.compile(r"(?P<punt>[\.:;!\?]) (?P<head>[A-Z])")

for line in open('nlp.txt', 'r'):
    l = line.strip()
    if not l: continue

    # \g<name>は名前付きグループの置換
    print punt.sub(r"\g<punt>\n\g<head>", l)
