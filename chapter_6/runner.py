# -*- coding: utf-8 -
import re

pattern = "(?<=[\.;:\?\!])"
repatter = re.compile(pattern)

for line in open('nlp.txt', 'r'):
    list = repatter.split(line)
    print list

    # for str in list:
    #     print str + "\n"
