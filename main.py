#!/usr/bin/env python
""" call with filename of file to be analyzed """
import sys
import os
import textstat
import stats
import structure
import listcheck

#read infile 
infile = sys.argv[1]
reqfile = str(os.path.dirname(infile) + "/reqs.txt")
forbidden = str(os.path.dirname(infile) + "/forbidden.txt")
desired = str(os.path.dirname(infile) + "/moneykw.txt")

stats.wordcount(infile)
stats.readability(infile)
structure.wellformed(infile, reqfile)
print(listcheck.listcheck(infile, forbidden))
print(listcheck.listcheck(infile, desired))
