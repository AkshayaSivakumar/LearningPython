# -*- coding: utf-8 -*-
"""
Created on Sat May 15 20:30:15 2021

@author: Akshaya V S
"""
import sys

filename = sys.argv[1]

text_file = open(filename)

words = {}

for line in text_file:
    for word in line.lower().split():
        word = word.strip("'?,.;!-/\"")
        if word not in words:
            words[word] = 0
        words[word] = words[word] + 1
        
text_file.close()

print("List of words in the file with number of times each appears.")
word_list = sorted(words)
for word in word_list:
    print(words[word], word)
