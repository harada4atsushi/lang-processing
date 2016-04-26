# -*- coding: utf-8 -
import re

class WordSplitter:
    def __init__(self, filename):
        self.filename = filename
        self.parse()

    def parse(self):
      self.parse_sentences()
      self.parse_words()

    def parse_sentences(self):
        # パターンの最初にrを付けると、バックスラッシュ文字をそのままバックスラッシュとして扱えるようになる
        # ?Pは名前付きグループにする構文
        punt = re.compile(r"(?P<punt>[\.:;!\?]) (?P<head>[A-Z])")
        self.sentences = []

        for line in open(self.filename, 'r'):
            l = line.strip()
            if not l: continue

            # \g<name>は名前付きグループの置換
            self.sentences.append(punt.sub(r"\g<punt>\n\g<head>", l))

    def parse_words(self):
        self.words = []
        # 51. 空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．
        for line in self.sentences:
            words = line.split(' ')
            for word in words:
                self.words.append(word)
            self.words.append("\n")
