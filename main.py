#!/usr/bin/env python
""" call with filename of file to be analyzed """
import sys
import os
import textstat
import stats
from structure import Structure
from pretty import print_matches, print_filtered_matches
from docgen import MainDoc
from matchbuilder import KW_Matcher

#read infile 
infile = sys.argv[1]
keyfile = sys.argv[2]
reqfile = str(os.path.dirname(infile) + "/req/reqs.txt")
forbidden = str(os.path.dirname(infile) + "/req/forbidden.txt")
desired = str(os.path.dirname(infile) + "/req/moneykw.txt")

statfile = MainDoc(infile).docgen()
rd = stats.readability(statfile)

struc = Structure(infile, reqfile)

main_spacy_doc = MainDoc(infile).spacy_doc()
fmatch = KW_Matcher(main_spacy_doc, forbidden).match_doc()
dmatch = KW_Matcher(main_spacy_doc, desired).match_doc()

print("="*70)
print(" +++ Textstatistik +++")
print("-"*70)
print("Text ist {0:4d} Worte lang.".format(stats.wordcount(statfile)))
print("Flesch Index: {0:5.2f}\nWiener Sachtextformel: {1:5.2f}\n".format(rd[0], rd[1]))

print("-"*70)
print(" +++ Anforderungen erfüllt? +++")
for k, v in struc.wellformed().items():
    print("{}:\t{}".format(k, v))

print("-"*70)
print_filtered_matches("Verbotene Worte", fmatch)
print("\n")
print_filtered_matches("MoneyKeywords", dmatch)

print("\n", "-"*70)
print(" +++ Keywordzählung +++")
print("-"*70)
pmatch = KW_Matcher(main_spacy_doc, keyfile)

for term, sk in pmatch.subkeys().items():
    print("\"{}\" ist Bestandteil von folgenden Phrasen: \"{}\"".format(term, ", ".join(sk)))
print("\n")

for term, found in pmatch.primary_matches(struc.structure()).items():
    print("{}:\t{}".format(term, found))

print("\n")
print_matches("Keywords gefunden", pmatch.match_doc())

print("="*70)
