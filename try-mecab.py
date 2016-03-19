# -*- coding: utf-8 -
lines = []
morphemes = []

for line in open('neko.txt.mecab', 'r'):
  list = line.split('\t')
  surface = list[0]

  if surface == "EOS\n":
    morphemes = []
    lines.append(morphemes)

  else:
    values = list[1].split(",")
    dict = {
      "surface": surface,
      "base": values[6],
      "pos": values[0],
      "pos1": values[1]
    }
    morphemes.append(dict)

print("surface: " + lines[1][1]['surface'])
print("base: " + lines[1][1]['base'])
print("pos: " + lines[1][1]['pos'])
print("pos1: " + lines[1][1]['pos1'])
