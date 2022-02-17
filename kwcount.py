""" module for keyword count """
import spacy
from spacy.matcher import Matcher

def kw_count(infile, kw_file):
    """ expects input: infile = a markdown file, kw_file = a text file containing one keyword per line
    :returns: how many times do the keywords contained in kw_file occur in the infile?
    """
    textfile = open(infile)
    keyfile = open(kw_file)

    text = textfile.read()
    keys_raw = keyfile.readlines()

    #strip newline char from raw keys
    keys = []
    for line in keys_raw:
        keys.append(line.rstrip())

    # set up nlp - or am I supposed to put this in a different function?
    nlp = spacy.load("de_core_news_sm")
    doc = nlp(text)

    # build patterns for matching

    # collect match count

    print("Keywords found: {}".format(key_found))
    return key_found
