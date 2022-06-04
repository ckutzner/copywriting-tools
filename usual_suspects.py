#!/usr/bin/env python
""" new module to check for forbidden and desired words """
import sys
import os
from matchbuilder import KW_Matcher

#read infile 
infile = sys.argv[1]
# keyfile = sys.argv[2]
# reqfile = str(os.path.dirname(infile) + "/req/reqs.txt")
forbidden = str(os.path.dirname(infile) + "/req/forbidden.txt")
desired = str(os.path.dirname(infile) + "/req/moneykw.txt")

print("\n", "-"*70)
print(" +++ Verbotene Worte gefunden: +++ ")
fmatch = KW_Matcher(infile, forbidden)

for word, found in fmatch.match_doc().items():
    if found[0] != 0:
        print("{}:\t{} mal gefunden".format(word, found[0]))
