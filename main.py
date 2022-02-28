#!/usr/bin/env python
""" call with filename of file to be analyzed """
import sys
import textstat
import stats
import structure
import listcheck

#read infile 
infile = sys.argv[1]
reqfile = sys.argv[2]
forbidden = sys.argv[3]
desired = sys.argv[4]

stats.wordcount(infile)
stats.readability(infile)
structure.wellformed(infile, reqfile)
print(listcheck.listcheck(infile, forbidden))
print(listcheck.listcheck(infile, desired))
