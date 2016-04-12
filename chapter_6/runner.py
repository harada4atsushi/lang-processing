# -*- coding: utf-8 -
# (. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．
import re

#punt = re.compile(r"(?P<punt>[\.:;!\?]) (?P<head>[A-Z])")
#punt = re.compile(r"(?P<punt>[\.:;!\?])")
#print punt

#pattern = "(?<=[\.;:\?\!])"
#repatter = re.compile(pattern)

#for line in open('nlp.txt', 'r'):
#    list = repatter.split(line)
#    print list

    # for str in list:
    #     print str + "\n"
