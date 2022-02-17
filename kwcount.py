""" module for keyword count """
import spacy
from spacy.matcher import Matcher

def kw_count(infile, kw_file):
    """ expects input: infile = a markdown file, kw_file = a text file containing one keyword per line
    :returns: how many times do the keywords contained in kw_file occur in the infile?
    """
    text = open(infile).read()
    keys_raw = open(kw_file).readlines()

    #strip newline char from raw keys
    keys = []
    for line in keys_raw:
        keys.append(line.rstrip())

    # set up nlp - or am I supposed to put this in a different function?
    nlp = spacy.load("de_core_news_sm")
    # prepare text for processing
    doc = nlp(text)

    # build patterns for matching
    kwpat = []
    for k in keys:
        kw = nlp(k)
        kwpat.append([w.lemma_ for w in kw])

    # collect match count

    print("Keywords found: {}".format(key_found))
    return key_found
