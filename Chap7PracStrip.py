#!python3
# Chap7PracStrip
# Remove whitespace from beginning and end of string using regex

import re

def remspace(string):
	print(string.strip())
	
remspace('   here is the   ')
