""" module for wellformedness analysis """
import re

def structure(infile):
    """ function that dissects the text into its parts for wellformedness analysis
    :argument infile: the markdown file to be processed
    :returns: a tuple: meta title as a string, meta desc as a string, teaser as a string, header 1 as a string, headings 2-3 as a list of strings, paragraphs as a list of strings

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

def requirements(infile):
    """ function that reads desired lengths from a text file
    :returns: a tuple of lists with the desired lengths of title, meta, h1, teaser, headings

    """
    pass

def wellformed(infile):
    """ function that takes output of structure and compares it to ranges in output of requirements
    :returns: a list of yes/no values (requirement fulfilled or not fulfilled)

    """
    struc = structure(infile)
    
    #hardcoding values for now: minimum and maximum length
    lengths = [[45, 55], [130, 160], [0, 80], [330, 350],[3,5]]
    wellformed = []

    for l in lengths:
        for s in struc:
            if len(s) >= l[0] and len(s) <= l[1]:
                wellformed.append("yes")
            else:
                wellformed.append("no")

    return wellformed

if __name__ == "__main__":
    struc = structure("testdata/testtext2.md")
    for s in struc:
        print(len(s))

if __name__ == "__main__":    
    print("test for requirements not written yet")

if __name__ == "__main__":
    if wellformed("testdata/testtext2.md") == ["no", "no", "yes", "no", "yes"]:
        print("test successful")
    else: 
        print("test failed")
