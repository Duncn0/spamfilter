# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 21:25:19 2021

@author: Dunca
"""
from os import listdir
from collections import Counter

#convert text into a list and make it all lowercase
def extract_words(text):
    splitwords = text.split()
    for i in range(len(splitwords)):
        
        splitwords[i] = splitwords[i].lower()
    
    return splitwords


spamfiles = listdir('spam/')
spamwords = []
print(spamfiles)

#open all the spam files and add all the words to a list
for file in spamfiles:
    myfile = open('spam/' + file, 'r')
    try:
        wordtokens = extract_words(myfile.read())
        spamwords.extend(wordtokens)
    except:
        print('This file could not be read.')

#create a dictionary of the spam words
spamcounts = Counter(spamwords)
print(spamcounts)

hamfiles = listdir('ham/')
hamwords = []
print(hamfiles)

#open all the ham files and add all the words to a list
for file in hamfiles:
    myfile = open('ham/' + file, 'r')
    try:
        wordtokens = extract_words(myfile.read())
        hamwords.extend(wordtokens)
    except:
        print('This file could not be read.')
    myfile.close()

#create a dictionary of the spam words
hamcounts = Counter(hamwords)
print(hamcounts)

