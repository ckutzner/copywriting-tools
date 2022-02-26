#!/usr/bin/env python
""" call with filename of file to be analyzed """
import sys
import textstat
import stats
import structure

#read infile 
infile = sys.argv[1]
reqfile = sys.argv[2]

stats.wordcount(infile)
stats.readability(infile)
structure.wellformed(infile, reqfile)
