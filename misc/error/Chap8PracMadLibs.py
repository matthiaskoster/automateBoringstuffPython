#! \usr\bin\env python3

# Chapter 8 Practice Mad Libs

# Replaces all ADJECTIVE, NOUN, ADVERB, VERB keywords with user input in text.

import re
import os

madLibFile = open('madlibs.txt')
madLibContents = madLibFile.read()

# TODO: Find and replace ADJECTIVE, NOUN, ADVERB, VERB with user substitutes.
adjectiveRegex = re.compile(r'ADJECTIVE*')
nounRegex = re.compile(r'NOUN*')
adverbRegex = re.compile(r'ADVERB*')
verbRegex = re.compile(r'VERB*')

if adjectiveRegex.search(madLibContents):
    for i in range(len(adjectiveRegex.findall(madLibContents))):
        print('Enter an adjective:')
        adjsub = input()
        madLibContents = adjectiveRegex.sub(adjsub, madLibContents, count=i-1)

# TODO: Get ADJECTIVE, NOUN, ADVERB, VERB substitutes from user input

# TODO: Save new string as new text file

# TODO: Print text to screen
print(madLibContents)

madLibFile.close()
