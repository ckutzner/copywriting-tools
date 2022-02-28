""" module to check for forbidden and desired words """
import spacy
from spacy.matcher import Matcher

def listcheck(infile, listfile):
    """ reads listfile, looks for matches of the lemma in infile
    arguments: infile - an text or markdown file, listfile - a textfile with one word to check per line
    :returns: each word from the list that was found

    """
    # prepare spacy
    nlp = spacy.load("de_core_news_sm")
    matcher = Matcher(nlp.vocab)
    # prepare match list
    found_words = []
    
    # read listfile
    list_file = open(listfile)
    lfile = list_file.read()
    # read infile & prepare for processing by spacy - externalize this to a different function for speed reasons!
    in_file = open(infile)
    ifile = in_file.read()
    doc = nlp(ifile)

    # make pattern for matching
    words = nlp(lfile)
    for token in words:
        if token.text != "\n":
            pattern = [{"LEMMA": token.lemma_}]
            matcher.add(token.text, [pattern])

    # match infile
    matches = matcher(doc)
    
    for match_id, start, end in matches:
        m = doc[start:end].text
        if m not in found_words:
            found_words.append(m)

    # close files, return matches and count
    in_file.close()
    list_file.close()
    return found_words

if __name__ == "__main__":
    if listcheck("testdata/testtext2.md", "testdata/forbidden.txt") == []:
        print("function did nothing!")
    else:
        for line in listcheck("testdata/testtext2.md", "testdata/forbidden.txt"):
            print("Forbidden word {} found!".format(line))
