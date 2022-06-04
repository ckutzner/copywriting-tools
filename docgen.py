""" module for SpaCy document generation """
import spacy

nlp = spacy.load("de_core_news_sm") # load SpaCy pipeline


class MainDoc:

    """Returns the whole document as a SpaCy object to perform matching operations on. """

    def __init__(self, docfile):
        """:docfile: document to be processed, a text or markdown file. """
        
        self.docfile = docfile

    def docgen(self):
        """generate an object from a text file.

        :returns: a read() object

        """
        # prepare document
        with open(self.docfile, encoding = "utf-8") as txt:
            text = txt.read()
       
        return text

    def spacy_doc(self):
        """Generate SpaCy doc.
        :returns: spacy doc

        """
        # prepare document
        with open(self.docfile, encoding = "utf-8") as txt:
            text = txt.read()
        
        # prepare text for processing
        doc = nlp(text)

        return doc


if __name__ == "__main__":
    text = MainDoc("testdata/testtext.md")
    print(text.docgen()[0:10])
    print(text.spacy_doc()[0:10])
