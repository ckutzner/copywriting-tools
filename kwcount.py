""" module for keyword count """
import spacy
from spacy.matcher import Matcher

def prepare_text_obj(infile):
    """ prepares a text for processing

    :infile: a markdown file
    :returns: a text object prepared for matching via SpaCy

    """
    with open(infile) as txt:
        text = txt.read()
    
    # set up nlp - or am I supposed to put this in a different function?
    nlp = spacy.load("de_core_news_sm")
    # prepare text for processing
    doc = nlp(text)

    return doc

def prepare_patterns(kw_file):
    """ prepares patterns for keyword matching

    :kw_file: a text file containing one keyword per line
    :returns: a matcher object

    """
    nlp = spacy.load("de_core_news_sm")
    matcher = Matcher(nlp.vocab)

    # initialize SpaCy matcher
    with open(kw_file) as file:
        keys = file.readlines()

    # build patterns for matching - todo: this should be its own function that returns a pattern for matching!
    kwpat = []
    for k in keys:
        kw = nlp(k.strip())
        kwpat.append([w.lemma_ for w in kw])

    return kwpat
 
def kw_match(textobj, matcher):
    """ returns matches of a keyword in a given text object
    :textobj: a nlp object of the text to be matched
    :matcher: a prepared SpaCy matcher
    :returns: a dictionary: keywords, matched or not? 
    """
    # build a dictionary for the keywords - can I extract those from the matcher object?
    keys_found = {}

    # collect match count

    print("Keywords found: {}".format(keys_found))
    return keys_found

if __name__ == "__main__":
    print(prepare_text_obj("testdata/testtext2.md")[0:5])
    print(prepare_patterns("testdata/kw.txt"))
