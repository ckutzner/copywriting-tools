""" module for building matcher patterns"""
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("de_core_news_sm") # load SpaCy pipeline

class KW_Matcher:

    """Builds matching patterns from a text file that contains a list of key phrases, one phrase per line
    TODO: Make subclass for primary keyword matching """

    def __init__(self, docfile, keyfile):
        """init 
        :docfile: document to be checked, a markdown file
        :keyfile: a text file containing phrases to be matched for, one
        key phrase per line
        """
        self.docfile = docfile
        self.keyfile = keyfile
        
        # read in keyfile
        with open(self.keyfile, encoding = "utf-8") as kf:
             self.keys = kf.readlines()
       
        # isolate multiword phrases
        self.multi_word = [k.strip() for k in self.keys if len(k.split()) > 1]

        # isolate single-word keywords
        self.single_word = [k.strip() for k in self.keys if len(k.split()) == 1]

    def subkeys(self):
        """warn of keywords that are subset of other keys.

        :returns: a dictionary 

        """
        subkeys = {}

        for w in self.multi_word:
            sub = [k.strip() for k in self.keys if k.strip() not in self.multi_word and k.strip() in w.split()]
            for s in sub:
                if s not in subkeys:
                    subkeys[s] = []
                    subkeys[s].append(w)
                else:
                    subkeys[s].append(w)
                    
        return subkeys

    def match(self):
        """ prepares patterns for keyword matching, prepares document,
        matches and returns keyword 

        :returns: dictionary with keywords as keys, their count and
        found matches as values
        """
        matcher = Matcher(nlp.vocab)        # prepare Matcher
        found_words = {}
        
        # prepare document
        with open(self.docfile, encoding = "utf-8") as txt:
            text = txt.read()
        
        # prepare text for processing
        doc = nlp(text)

        # match pattern generation for single words
        words = nlp(" ".join(self.single_word))
        for token in words:
            if token.text != "\n":
                pattern = [{"LEMMA": token.lemma_}]
                matcher.add(token.text, [pattern])

        # matcher for multi-word keywords
        for term in self.multi_word:
            pattern = []
            wrds = nlp(term)
            for token in wrds[:-1]:
                pattern.extend([{"LEMMA": token.lemma_}, {"is_stop": True, "op": "?"}])

            pattern.extend([{"LEMMA": wrds[-1].lemma_}])

            matcher.add(term, [pattern])

        #match infile
        matches = matcher(doc)
    
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]
            m = doc[start:end].text
            if string_id not in found_words:
                found_words[string_id] = [1, m]
            else:
                found_words[string_id][0] += 1
                if m not in found_words[string_id][1:]:
                    found_words.append(m)

        return found_words


if __name__ == "__main__":
    kwmatch = KW_Matcher("testdata/testtext2.md", "testdata/req/moneykw.txt")
    if kwmatch.match() == {'offensiv': [4, 'offensiv'], 'Flasche':
        [4, 'Flasche'], 'drei': [4, 'drei']}:
        print("matcher test successful")
    else:
        print("matcher test failed")

    submatch = KW_Matcher("testdata/testtext.md", "testdata/kw.txt")
    print(submatch.subkeys())
