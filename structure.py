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
    lines_raw = file.readlines()
    lines = list(filter(lambda x: not re.match(r'^\s*$', x), lines_raw))
    
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
    """ function that reads desired lengths from a text file that has min and max on one line each
    :returns: a nested list with the desired lengths of title, meta, h1, teaser, headings

    """
    file = open(infile)
    req = file.readlines()

    # remove whitespace and turn each number into an integer, return a nested array
    reqs = []
    for r in req:
        temp = r.strip().split(", ")
        reqs.append([int(temp[0]), int(temp[1])])

    file.close()
    return reqs

def wellformed(infile, reqfile):
    """ function that takes output of structure and compares it to ranges in output of requirements, given a requirement file
    :returns: a list of yes/too short/too long strings (requirement fulfilled or not fulfilled)

    """
    struc = structure(infile)
    lengths = requirements(reqfile)
    
    well_formed = []
    labels = ["meta title", "meta description", "h1", "teaser", "number of h2s"]

    for i in range(0, 5):
        if lengths[i][0] <= len(struc[i]) <= lengths[i][1]:
            well_formed.append("yes")
        if len(struc[i] < lengths[i][0]:
            well_formed.append("too short")
        else:
            well_formed.append("too long")
    
    #print("requirements met: \n", labels, "\n", well_formed)

    return well_formed

if __name__ == "__main__":
    struc = structure("testdata/testtext2.md")
    for s in struc:
        print(len(s))

if __name__ == "__main__":
    if requirements("testdata/reqs.txt") == [[45, 55], [130, 160], [0, 80], [330, 350],[3,5]]:
        print("test for requirements successful! \n")
    else:
        print("test for requirements failed. \n")

if __name__ == "__main__":
    print(wellformed("testdata/testtext2.md", "testdata/reqs.txt"))
    if wellformed("testdata/testtext2.md", "testdata/reqs.txt") == ["no", "no", "yes", "no", "yes"]:
        print("test successful")
    else: 
        print("test failed")
