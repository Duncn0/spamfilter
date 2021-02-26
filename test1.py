# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 09:05:19 2021

@author: Duncan
"""
from os import listdir
from collections import Counter
import string

#convert text into a list and make it all lowercase
def extract_words(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    splitwords = text.split()
    for i in range(len(splitwords)):
        
        splitwords[i] = splitwords[i].lower()
    
    return splitwords

def openfile(folder):
    dirlist = listdir(folder)
    words = []
    for file in dirlist:
        myfile = open(folder + file, 'r')
        try:
            wordtokens = extract_words(myfile.read())
            words.extend(wordtokens)
        except:
            print('This file could not be read.')
        myfile.close()
    return words

#counting number of ham and spam test data
numberofham = len(listdir('spam/'))
numberofspam = len(listdir('ham/'))

#open all the spam files and add all the words to a list
spamwords = openfile('spam/')
#print(spamwords)

#create a dictionary of the spam words
spamcounts = Counter(spamwords)
#print(spamcounts)

#open all the ham files and add all the words to a list
hamwords = openfile('ham/')
#print(hamwords)

#create a dictionary of the spam words
hamcounts = Counter(hamwords)
#print(hamcounts)

#find spamicity of each word
spamicitydic = {'word': 'probspam'}
for w in spamcounts:
    spamicitydic[w] = spamcounts[w]/len(spamwords)
#print(spamicitydic)

#find hamicity of each word
hamicitydic = {'word': 'probham'}
for w in hamcounts:
    hamicitydic[w] = hamcounts[w]/len(hamwords)
#print(hamicitydic)


totalmessages = numberofham + numberofspam
ProbHamEmail = numberofham/totalmessages
ProbSpamEmail = numberofspam/totalmessages

testfile = open('ham/0070.1999-12-27.farmer.ham.txt', 'r')
testwords = extract_words(testfile.read())
print(testwords)

SpamProbability = 1
for i in testwords:
    print(i, spamicitydic.get(i, 1))
    IndividualProbability = spamicitydic.get(i, 1)
    SpamProbability = SpamProbability * IndividualProbability

print(SpamProbability)

HamProbability = 1
for i in testwords:
    print(i, hamicitydic.get(i, 1))
    IndividualProbability = hamicitydic.get(i, 1)
    HamProbability = HamProbability * IndividualProbability
print(HamProbability)