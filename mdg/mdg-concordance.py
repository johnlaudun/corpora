#! /usr/bin/env python

import nltk
import sys

# First, let's get the word from the user:

print "Enter the word you would like to see in context:",
word = raw_input()

# Then we need the base text:

thefile = open('mdg.txt')
text = thefile.read(thefile)

concordword = text.concordance(word)

Print(concordword)