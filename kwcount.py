""" module for keyword count """
import spacy

def kw_count(infile, kw_file):
    """ expects input: infile = a markdown file, kw_file = a text file containing one keyword per line
    :returns: how many times do the keywords contained in kw_file occur in the infile?
    """
    textfile = open(infile)
    keyfile = open(kw_file)

    text = textfile.read()
    keys = keyfile.readlines()

    print("Keywords found: {}".format(key_found))
    return key_found
