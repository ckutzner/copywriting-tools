""" module to check for forbidden and desired words """
import spacy

def listcheck(infile, listfile):
    """ reads listfile, looks for matches of the lemma in infile, counts matches
    arguments: infile - an text or markdown file, listfile - a textfile with one word to check per line
    :returns: each word from the list that was found + word as a list of tuples

    """
    # read listfile
    lfile = listfile.read()
    # read infile & prepare for processing by spacy - externalize this to a different function for speed reasons!
    ifile = infile.read()

    # make pattern for matching
    lines = lfile.split("\n")

    # match infile
    # close files, return matches and count
    ifile.close()
    lfile.close()
    return matchcount

if __name__ == "__main__":
    for l in listcheck("testdata/testtext2.md", "testdata/forbidden.txt"):
        print("Forbidden word {} found {} times".format(l[0], l[1]));
