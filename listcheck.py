""" module to check for forbidden and desired words """
import spacy
from spacy.matcher import Matcher

# prepare spacy
nlp = spacy.load("de_core_news_sm")
matcher = Matcher(nlp.vocab)

def listcheck(infile, listfile):
    """ reads listfile, looks for matches of the lemma in infile
    arguments: infile - an text or markdown file, listfile - a textfile with one word to check per line
    :returns: each word from the list that was found

    """
    # prepare match list
    found_words = []
    
    # read listfile
    with open(listfile, encoding = "utf-8") as list_file:
        keys = list_file.readlines()

    # read infile & prepare for processing by spacy - externalize this to a different function for speed reasons!
    with open(infile, encoding = "utf-8") as in_file:
        ifile = in_file.read()

    doc = nlp(ifile)
    
    # isolate multiword phrases
    multi_word = [k for k in keys if len(k.split()) > 1]

    # isolate single-word keywords
    single_word = [k for k in keys if len(k.split()) == 1]

    # match pattern generation for single words
    words = nlp(" ".join(single_word))
    for token in words:
        if token.text != "\n":
            pattern = [{"LEMMA": token.lemma_}]
            matcher.add(token.text, [pattern])

    # matcher for multi-word keywords
    for term in multi_word:
        pattern = []
        wrds = nlp(term)
        for token in wrds[:-1]:
            pattern.extend([{"LEMMA": token.lemma_}, {"is_stop": True, "op": "?"}])

        pattern.extend([{"LEMMA": wrds[-1].lemma_}])

        matcher.add(term, [pattern])

    # match infile
    matches = matcher(doc)
    
    for match_id, start, end in matches:
        m = doc[start:end].text
        if m not in found_words:
            found_words.append(m)

    # return matches
    return found_words

if __name__ == "__main__":
    if listcheck("testdata/testtext2.md", "testdata/req/forbidden.txt") == []:
        print("function did nothing!")
    else:
        for line in listcheck("testdata/testtext2.md", "testdata/req/forbidden.txt"):
            print("Forbidden word {} found!".format(line))
