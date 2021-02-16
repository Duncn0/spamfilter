# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 21:25:19 2021

@author: Dunca
"""
from os import listdir
from collections import Counter


def extract_words(text):
    splitwords = text.split()
    for i in range(len(splitwords)):
        
        splitwords[i] = splitwords[i].lower()
    
    return splitwords


spamfiles = listdir('spam/')
spamwords = []
print(spamfiles)

for file in spamfiles:
    myfile = open('spam/' + file, 'r')
    try:
        wordtokens = extract_words(myfile.read())
        spamwords.extend(wordtokens)
    except:
        print('This file could not be read.')

spamcounts = Counter(spamwords)
print(spamcounts)

hamfiles = listdir('ham/')
hamwords = []
print(hamfiles)

for file in hamfiles:
    myfile = open('ham/' + file, 'r')
    try:
        wordtokens = extract_words(myfile.read())
        hamwords.extend(wordtokens)
    except:
        print('This file could not be read.')
    myfile.close()

hamcounts = Counter(hamwords)
print(hamcounts)

