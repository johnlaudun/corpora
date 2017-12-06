#! /usr/bin/env python

# First I need the Natural Language Toolkit
import nltk

# Now I need to open the file and read it

thefile = open('mdg.txt')
textraw = thefile.read()
textlist = textraw.split()
fdist = FreqDist(textlist)

# 2012-02-05-1339
# I keep getting an error on "FreqDist", 
# as if Python doesn't know what it is.

tempfile = open('mdg-frequency.txt', 'w')
tempfile.write(','.join(vocabulary))
tempfile.close()