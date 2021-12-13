#!/usr/bin/env python
""" call with filename of file to be analyzed """
import sys
import textstat
import stats

#read infile 
infile = sys.argv[1]

stats.wordcount(infile)
stats.readability(infile)
