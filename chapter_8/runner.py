# -*- coding: utf-8 -
from stop_word import StopWord

stop_word = StopWord()
print stop_word.exists("is")
print stop_word.exists("hoge")
