""" module for wellformedness analysis """
import re

def structure(infile):
    """ function that dissects the text into its parts for wellformedness analysis
    :argument infile: the markdown file to be processed
    :returns: a tuple: meta title as a string, meta desc as a string, header 1 as a string, headings 2-3 as a list of strings, paragraphs as a list of strings

    """
    # set up lists
    headings = []
    paragraphs = []

    # read text
    file = open(infile)
    lines = file.readlines()
    
    for l in lines:
        if lines.index(l) == 0:
            title = l.rstrip()
        if lines.index(l) == 1:
            metadesc = l.rstrip()
        if re.match(r'^\#{1}\s\w', l):
            h1 = l.strip('# \n')
        if re.match(r'^\#{2,3}\s\w', l):
            headings.append(l.strip('# \n'))
        if lines.index(l) == 3:
            teaser = l.rstrip()
        else:
            if lines.index(l) > 3 and re.match(r'^\w', l):
                paragraphs.append(l)

    file.close()
    # todo: transform this into a dictionary
    return title, metadesc, h1, teaser, headings, paragraphs

if __name__ == "__main__":
    struc = structure("testdata/testtext.md")
    for s in struc:
        print(len(s))
