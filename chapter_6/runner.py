# -*- coding: utf-8 -
import re

#pattern = ".*[\.;:\?_!]."
#pattern = "(.*\.)"
#repatter = re.compile(pattern)

str = "aiueo kakikuleko hoge: hoge. waaaaaay. togetoge"
contactInfo = 'Doe, John: 555-1212'

#list = repatter.findall(contactInfo)
#match = re.search(r'(\w+), (\w+): (\S+)', contactInfo)
list = re.findall('.+[\.]', str)
print list

# for line in open('nlp.txt', 'r'):
#     list = repatter.findall(line)
#     print list
#     strings = repatter.split(line)
#
#     for str in strings:
#         print str + "\n"
