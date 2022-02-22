""" module for wellformedness analysis """
import re

def structural(infile):
    """ function that dissects the text into its parts for wellformedness analysis
    :argument infile: the markdown file to be processed
    :returns: meta title as a string, meta desc as a string, header 1 as a string, headings 2-3 as a list, paragraphs as a list

    """
    # set up lists
    headings = []
    paragraphs = []

    # read text
    lines = open(infile).readlines()
    
    for l in lines:
        if lines.index(l) == 0:
            title = l.rstrip()
        else if lines.index(l) == 1:
            metadesc = l.rstrip()
        else if re.match(r'^\#{1}\s\w', l):
            h1 = l.strip('# \n')
        else if re.match(r'^\#{2,3}\s\w', l):
            headings.append(l.rstrip('# \n'))
        else if lines.index(l) == 3:
            teaser = l.rstrip()
        else:
            paragraphs.append(l)

    # close infile
    lines.close()
    return title, metadesc, h1, teaser, headings, paragraphs
