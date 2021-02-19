# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 09:05:19 2021

@author: Duncan
"""
from os import listdir
from collections import Counter

#convert text into a list and make it all lowercase
def extract_words(text):
    splitwords = text.split()
    for i in range(len(splitwords)):
        
        splitwords[i] = splitwords[i].lower()
    
    return splitwords

#counting number of ham and spam test data
numberofham = len(listdir('spam/'))
numberofspam = len(listdir('ham/'))


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
        myfile.close()

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

#find spamicity of each word
spamicitydic = {'word': 'probspam'}
for w in spamcounts:
    spamicitydic[w] = spamcounts[w]/len(spamwords)
print(spamicitydic)

#find hamicity of each word
hamicitydic = {'word': 'probham'}
for w in hamcounts:
    hamicitydic[w] = hamcounts[w]/len(hamwords)
#print(hamicitydic)


totalmessages = numberofham + numberofspam
ProbHamEmail = numberofham/totalmessages
ProbSpamEmail = numberofspam/totalmessages

testfile = 'levis is'
testlist = extract_words(testfile)

probspam = ProbSpamEmail
for w in testlist:
    print(spamicitydic[w])
    try:
        probspam = probspam * spamicitydic[w]
    except:
        print('Error')     
print('The probability this email is spam is ' + str(probspam))

probham = ProbHamEmail
for w in testlist:
    probham = probham * hamicitydic[w]
print('The probability this email is ham is ' + str(probham))

if probham > probspam:
    print('This message is ham')
else:
    print('This message is spam')
