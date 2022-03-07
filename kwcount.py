""" module for keyword count """
import spacy
from spacy.matcher import Matcher

def prepare_text_obj(infile):
    """ prepares a text for processing

    :infile: a markdown file
    :returns: a text object prepared for matching via SpaCy

    """
    text = open(infile).read()
    
    # set up nlp - or am I supposed to put this in a different function?
    nlp = spacy.load("de_core_news_sm")
    # prepare text for processing
    doc = nlp(text)

    text.close()
    return doc
 
def kw_match(textobj, kw_file):
    """ returns matches of a keyword in a given text object
    :kw_file: a text file containing one keyword per line
    :returns: how many times do the keywords contained in kw_file occur in the infile?
    """
    keys_raw = open(kw_file).readlines()

    #strip newline char from raw keys
    keys = []
    for line in keys_raw:
        keys.append(line.rstrip())

    # build patterns for matching - todo: this should be its own function that returns a pattern for matching!
    kwpat = []
    for k in keys:
        kw = nlp(k)
        kwpat.append([w.lemma_ for w in kw])

    # collect match count

    print("Keywords found: {}".format(key_found))
    return key_found
