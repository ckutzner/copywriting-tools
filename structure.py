""" module for wellformedness analysis """
import re

def structure(infile):
    """ function that dissects the text into its parts for wellformedness analysis
    :argument infile: the markdown file to be processed
    :returns: a tuple: meta title as a string, meta desc as a string, teaser as a string, header 1 as a string, headings 2-3 as a list of strings, first paragraph as a string 

    """
    # set up list of headings
    headings = []

    # read text
    with open(infile) as file:
        lines_raw = file.readlines()

    lines = [line for line in lines_raw if not re.match(r'^\s*$', line)]
    
    for l in lines:
        if lines.index(l) == 0:
            title = l.strip()
        if lines.index(l) == 1:
            metadesc = l.strip()
        if re.match(r'^\#{1}\s\w', l):
            h1 = l.strip('# \n')
        if re.match(r'^\#{2,3}\s\w', l):
            headings.append(l.strip('# \n'))
        if lines.index(l) == 3:
            teaser = l.strip()
        if lines.index(l) == 5:
            first_par = l.strip()
        else:
            if lines.index(l) > 3 and re.match(r'^\w', l):
                pass

    # todo: transform this into a dictionary
    return title, metadesc, h1, teaser, headings, first_par

def requirements(infile):
    """ function that reads desired lengths from a text file that has min and max on one line each
    :returns: a nested list with the desired lengths of title, meta, h1, teaser, headings

    """
    with open(infile) as file:
        req = file.readlines()

    # remove whitespace and turn each number into an integer, return a nested array
    reqs = []
    for r in req:
        temp = r.strip().split(", ")
        reqs.append([int(temp[0]), int(temp[1])])

    return reqs

def wellformed(infile, reqfile):
    """ function that takes output of structure and compares it to ranges in output of requirements, given a requirement file
    :returns: a list of yes/no values (requirement fulfilled or not fulfilled)

    """
    struc = structure(infile)
    lengths = requirements(reqfile)
    
    well_formed = []
    labels = ["meta title", "meta description", "h1", "teaser", "number of h2s"]

    for i in range(0, 5):
        if lengths[i][0] <= len(struc[i]) <= lengths[i][1]:
            well_formed.append("yes")
        else:
            well_formed.append("no")
    
    print("requirements met: \n", labels, "\n", well_formed)

    return well_formed

if __name__ == "__main__":
    struc = structure("testdata/testtext2.md")
    for s in struc:
        print(len(s))
    print(struc[-1])

if __name__ == "__main__":
    if requirements("testdata/reqs.txt") == [[45, 55], [130, 160], [0, 80], [330, 350],[3,5]]:
        print("test for requirements successful! \n")
    else:
        print("test for requirements failed. \n")

if __name__ == "__main__":
    print(wellformed("testdata/testtext2.md", "testdata/reqs.txt"))
    if wellformed("testdata/testtext2.md", "testdata/reqs.txt") == ["no", "no", "yes", "no", "yes"]:
        print("wellformedness test successful")
    else: 
        print("wellformedness test failed")
