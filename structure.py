""" module for wellformedness analysis """
import re
import textstat

class Structure:

    """Docstring for Structure. """

    def __init__(self, docfile, reqfile):
        """init 
        :docfile: a text or markdown file
        :reqfile: a text file containing the requirements
        """
        self.docfile = docfile
        self.reqfile = reqfile
        

    def structure(self):
        """ function that dissects the text into its parts for wellformedness analysis
        :argument infile: the markdown file to be processed
        :returns: a tuple: meta title as a string, meta desc as a string, teaser as a string, header 1 as a string, headings 2-3 as a list of strings, first paragraph as a string 

        """
        # set up list of headings
        headings = []

        # read text
        with open(self.docfile, encoding = "utf-8") as file:
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

        return title, metadesc, h1, teaser, headings, first_par


    def requirements(self):
        """ function that reads desired lengths from a text file that has min and max on one line each
        :returns: a nested list with the desired lengths of title, meta, h1, teaser, headings

        """
        with open(self.reqfile, encoding = "utf-8") as file:
            req = file.readlines()

        # remove whitespace and turn each number into an integer, return a nested array
        reqs = []
        for r in req:
            temp = r.strip().split(", ")
            reqs.append([int(temp[0]), int(temp[1])])

        return reqs


    def wellformed(self):
        """ function that takes output of structure and compares it to ranges in output of requirements, given a requirement file
        :returns: a list of yes/too short/too long strings (requirement fulfilled or not fulfilled)

        """
        struc = self.structure()
        lengths = self.requirements()
        
        well_formed = []
        labels = ["meta title", "meta description", "h1", "teaser", "number of h2s"]

        for i in range(0, len(labels)-1):
            count = textstat.char_count(struc[i], ignore_spaces = "false") 
            if count < lengths[i][0]:
                well_formed.append("too short")
            if count > lengths[i][1]:
                well_formed.append("too long")
            else:
                well_formed.append("yes")
        
        if len(struc[4]) < lengths[-1][0]:
            well_formed.append("too few")
        if len(struc[4]) > lengths[-1][1]:
            well_formed.append("too many")
        else:
            well_formed.append("ok")

        wf = dict(zip(labels, well_formed))
        return wf

if __name__ == "__main__":
    struc = Structure("testdata/testtext2.md", "testdata/req/reqs.txt")

    for s in struc.structure():
        print(len(s))
    print(struc.structure()[-1])

    if struc.requirements() == [[45, 55], [130, 160], [0, 80], [330, 350],[3,5]]:
        print("test for requirements successful! \n")
    else:
        print("test for requirements failed. \n")

    print(struc.wellformed())
    if struc.wellformed() == {'meta title': 'too short', 'meta description': 'yes', 'h1': 'too short', 'teaser': 'yes', 'number of h2s': 'yes'}:
        print("wellformedness test successful")
    else: 
        print("wellformedness test failed")
