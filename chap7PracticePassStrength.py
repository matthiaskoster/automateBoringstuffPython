#! /usr/bin/env python3

# Practice Chap. 7
# Password Strength Tester

import re
import sys

def passStrengthTest(passWord):
    lowerRegex = re.compile(r'[a-z]')
    upperRegex = re.compile(r'[A-Z]')
    numRegex = re.compile(r'[0-9]')
    molower = lowerRegex.search(passWord)
    if len(passWord) < 8:
        print('Your password is less than 8 characters which is too short.')
    elif not molower:
        print('You need at least one lower case letter.')
    else:
        print('Your password is strong!')


print('What is your password?')
passW = input()
passStrengthTest(passW)

sys.exit()
