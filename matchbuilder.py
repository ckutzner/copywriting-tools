""" module for building matcher patterns"""
import spacy
from spacy.matcher import Matcher
from structure import Structure
from docgen import MainDoc          # just for the test

nlp = spacy.load("de_core_news_sm") # load SpaCy pipeline

class KW_Matcher:

    """Builds matching patterns from a text file that contains a list of key phrases, one phrase per line
    """

    def __init__(self, docfile, keyfile):
        """init 
        :docfile: a file object, the main document
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

    def match_doc(self):
        """ prepares patterns for keyword matching

        :returns: dictionary with keywords as keys, their count and
        found matches as values
        """
        matcher = Matcher(nlp.vocab)        # prepare Matcher
        found_words = {}
        
        doc = self.docfile

        # match pattern generation for single words
        words = nlp(" ".join(self.single_word))
        for token in words:
            if token.text != "\n":
                pattern = [{"LEMMA": token.lemma_}]
                matcher.add(token.text, [pattern])
                found_words[token.text] = [0]

        # matcher for multi-word keywords
        for term in self.multi_word:
            pattern = []
            wrds = nlp(term)
            for token in wrds[:-1]:
                pattern.extend([{"LEMMA": token.lemma_}, {"is_stop": True, "op": "?"}])

            pattern.extend([{"LEMMA": wrds[-1].lemma_}])

            matcher.add(term, [pattern])
            found_words[term] = [0]

        #match infile
        matches = matcher(doc)
    
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]
            m = doc[start:end].text
            found_words[string_id][0] += 1
            if m not in found_words[string_id][1:]:
                found_words[string_id].append(m)

        return found_words

    def primary_matches(self, struc):
        """checks for occurrence of primary keyword in the items returned by structure
        :struc: a Structure object, as returned by Structure.structure()

        :returns: a dictionary of item names, each with yes/no values 

        """
        # initialize matcher
        matcher = Matcher(nlp.vocab)

        # initialize dictionary for positions where kw was detected
        labels = ["meta title", "meta description", "h1", "teaser", "h2", "first paragraph"]
        found_pos = dict.fromkeys(labels, "no")

        # prepare the items to perform matching on
        items = list(struc)
        items[3] = str(items[3].split(". ")[0])      #isolate first sentence of teaser 
            
        for i in items:
            if isinstance(i, list):
                i = ", ".join(i)     # join together list items
            i = i.strip("#\n ")

        # put them in a dictionary with their labels
        lines_dic = dict(zip(labels, items))
            
        # isolate primary keyword
        primary_kw = self.keys[0].strip()
        
        # prepare the matcher
        if len(primary_kw.split(" ")) > 1:
            pattern = []
            words = nlp(primary_kw)
            for token in words[:-1]:
                pattern.extend([{"LEMMA": token.lemma_}, {"is_stop": True, "op": "?"}])
            pattern.extend([{"LEMMA": words[-1].lemma_}])
            matcher.add(primary_kw, [pattern])
        else:
            pattern = [{"LEMMA": str(primary_kw.strip())}]
            matcher.add(primary_kw, [pattern])

        # prepare the items for matching
        for line in lines_dic:
            doc = nlp(str(lines_dic[line]))
            if len(matcher(doc)) == 0:
                found_pos[line] = "no"
            else: 
                found_pos[line] = "keyword found"

        return found_pos


if __name__ == "__main__":
    file = MainDoc("testdata/testtext2.md").spacy_doc()
    kwmatch = KW_Matcher(file, "testdata/req/moneykw.txt")
    if kwmatch.match_doc()['offensiv'] == [4, 'offensiv'] and kwmatch.match_doc()['Flasche'] == [4, 'Flasche']:
        print("matcher test successful\n")
    else:
        print("matcher test failed\n")

    submatch = KW_Matcher(file, "testdata/kw.txt")
    if submatch.subkeys() == {'Heiterkeit': ['wunderbare Heiterkeit']}:
        print("submatch test successful\n")
    else:
        print("submatch test failed\n")
    
    prim_match = KW_Matcher(file, "testdata/kw.txt")
    pstruc = Structure("testdata/testtext.md", "testdata/req/reqs.txt").structure()
    if prim_match.primary_matches(pstruc) == {'meta title': 'keyword found', 'meta description': 'no', 'h1': 'keyword found', 'teaser': 'keyword found', 'h2': 'keyword found', 'first paragraph': 'keyword found'}:
        print("primary matching test successful\n")
    else:
        print("primary matching test failed\n")
