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

def print_filtered_matches(heading, dict):
    """ Pretty-print matches from a dictionary where the count is not zero.
    :returns: a pretty printout of a dictionary where the first item of the 
    values list is not zero.

    """
    print("\n", "-"*70)
    print(" +++ {} gefunden: +++ ".format(heading))
    for k, v in dict.items():
        if v[0] != 0:
            print("{}:\t{} mal gefunden".format(k, v[0]))

fmatch = KW_Matcher(infile, forbidden).match_doc()
dmatch = KW_Matcher(infile, desired).match_doc()

print_filtered_matches("Verbotene Worte", fmatch)
print_filtered_matches("MoneyKeywords", dmatch)
