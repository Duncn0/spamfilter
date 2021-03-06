# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 10:24:19 2021

@author: Dunca
"""
import os
from collections import Counter
import string
import math
import numpy as np
from tkinter.filedialog import askdirectory
from tkinter import *
import matplotlib
import matplotlib.pyplot as plt

#classifies all .txt files in a folder and sort them into a ham and spam folder
def classify_folder():
    root = Tk()
    new_folder = askdirectory()
    root.destroy()
    dirlist = os.listdir(new_folder)
    classified_dic = {}
    for file in dirlist:
        try:
            myfile = open(new_folder + '/' + file, 'r')
            word_tokens = extract_words(myfile.read())
            classification = calc_spam_ham_prob(word_tokens, ham_prob_dict, spam_prob_dict, initial_ham_prob, initial_spam_prob)[0]
            classified_dic.update({file:classification})
            myfile.close()
        except:
            print('This file could not be read.')
      
    spampath = new_folder + '\spam' 
    if not os.path.exists(spampath):
        os.makedirs(spampath)
    hampath = new_folder + '\ham' 
    if not os.path.exists(hampath):
        os.makedirs(hampath)
    
    for i in classified_dic:
        if classified_dic[i] == 'Ham':
            os.rename(new_folder + '/' + i, 
                      new_folder + '\ham/' + i)
        else:
            os.rename(new_folder + '/' + i, new_folder + '\spam/' + i )
    return classified_dic 

#test the classifier against known spam and ham emails and prints how many were correctly classified
def test_classifier(hamtest, spamtest):
    #calculates how many test emails were correctly classified
    correct_spam = 0
    for i in spamtest:
        testwords = extract_words(i)
        prob = calc_spam_ham_prob(testwords, ham_prob_dict, spam_prob_dict, initial_ham_prob, initial_spam_prob)
        if prob[0] == 'Spam':
            correct_spam = correct_spam + 1
        
    correct_ham = 0
    for i in hamtest:
        testwords = extract_words(i)
        prob = calc_spam_ham_prob(testwords, ham_prob_dict, spam_prob_dict, initial_ham_prob, initial_spam_prob)
        if prob[0] == 'Ham':
            correct_ham = correct_ham + 1
            
    percent_correct_spam = (correct_spam/len(spamtest)) * 100
    print(percent_correct_spam, '% of the spam test emails were correctly classified')
    
    percent_correct_ham = (correct_ham/len(hamtest)) * 100
    print(percent_correct_ham, '% of the ham test emails were correctly classified')
    return percent_correct_ham, percent_correct_spam

#calculates the the probability a text is ham and spam and classifies them
def calc_spam_ham_prob(testwords, ham_prob_dict, spam_prob_dict, initial_ham_prob, initial_spam_prob):
    SpamProbability = 0
    for i in testwords:
        IndividualProbability = math.log(spam_prob_dict.get(i, 1))
        SpamProbability = initial_spam_prob + IndividualProbability
    
    HamProbability = 0
    for i in testwords:
        IndividualProbability = math.log(ham_prob_dict.get(i, 1))
        HamProbability = initial_ham_prob + IndividualProbability
    if SpamProbability > HamProbability:
        classification = 'Spam'
    else:
        classification = 'Ham'
    return classification, SpamProbability, HamProbability

#creates the probability dictionaries used by the classifier
def create_prob_dicts(hamtrain, spamtrain):
    
    # counting number of ham and spam training data
    numberofham = len(hamtrain)
    numberofspam = len(spamtrain)

    # open all the ham files and add all the words to a list
    hamwords = []
    for i in hamtrain:
        hamwords.extend(extract_words(i))

    # open all the spam files and add all the words to a list
    spamwords = []
    for i in spamtrain:
        spamwords.extend(extract_words(i))
    
    allwords = list(set(spamwords + hamwords))
    # add one count to each word
    spamwords = spamwords + allwords
    hamwords = hamwords + allwords
    
    # creates dictionaries of the ham and spam words and how often they appear
    spamcounts = Counter(spamwords)
    hamcounts = Counter(hamwords)
    
    # creates dictionaries for the probabilities of each word being ham or spam
    spam_prob_dict = {'word': 'probspam'}
    for w in spamcounts:
        spam_prob_dict[w] = spamcounts[w] / len(spamwords)
    
    ham_prob_dict = {'word': 'probham'}
    for w in hamcounts:
        ham_prob_dict[w] = hamcounts[w] / len(hamwords)
    
    
    totalmessages = numberofham + numberofspam
    initial_ham_prob = math.log(numberofham / totalmessages)
    initial_spam_prob = math.log(numberofspam / totalmessages)
    return ham_prob_dict, spam_prob_dict, initial_ham_prob, initial_spam_prob

#turns text into a list of words and removes punctuation
def extract_words(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    #text = ''.join([i for i in text if not i.isdigit()])
    splitwords = text.split()
    for i in range(len(splitwords)):
        splitwords[i] = splitwords[i].lower()

    return splitwords

#creates a list of strings from each file for training and/or test data
def create_train_test(folder, seed=0):
    dirlist = os.listdir(folder)
    all = []
    for file in dirlist:
        try:
            myfile = open(folder + file, 'r')
            all.append(myfile.read())
            
        except:
            print("This file could not be read.")

    np.random.shuffle(all)

    train = all[0:int(0.8 * len(all))]
    test = all[int(0.8 * len(all)):] 
    return train, test


hamtest_correct = []
spamtest_correct = []
    
for z in range(20):
    np.random.seed(z)
    ham = create_train_test('ham/')
    spam = create_train_test('spam/')
    hamtrain = ham[0]
    spamtrain = spam[0]
    
    hamtest = ham[1]
    spamtest = spam[1]
    
    dicte = create_prob_dicts(hamtrain, spamtrain)
    ham_prob_dict = dicte[0]
    spam_prob_dict = dicte[1]
    
    initial_ham_prob = dicte[2]
    initial_spam_prob = dicte[3]
    
    classes = test_classifier(hamtest, spamtest)
    percham = classes[0]
    percspam = classes[1]
    hamtest_correct.append(percham)
    spamtest_correct.append(percspam)
    print(hamtest_correct)
    print(spamtest_correct)

labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, hamtest_correct, width, label='Correct Ham')
rects2 = ax.bar(x + width/2, spamtest_correct, width, label='Correct Spam')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Percent Correct (%)')
ax.set_title('Accuracy of Spam Classifier')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


fig.tight_layout()

plt.show()

































