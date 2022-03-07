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
reqfile = str(os.path.dirname(infile) + "/req/reqs.txt")
forbidden = str(os.path.dirname(infile) + "/req/forbidden.txt")
desired = str(os.path.dirname(infile) + "/req/moneykw.txt")

print("Text ist {0:4d} Worte lang.".format(stats.wordcount(infile)))
print("Flesch Index: {0:5.2f}\nWiener Sachtextformel: {1:5.2f}".format(stats.readability(infile)[0], stats.readability(infile)[1]))
print(structure.wellformed(infile, reqfile))
print(listcheck.listcheck(infile, forbidden))
print(listcheck.listcheck(infile, desired))
