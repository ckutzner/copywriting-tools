""" module for stats """
import textstat
from docgen import MainDoc

def wordcount(infile):
    """ count words

    :infile: a file object 
    :returns: wordcount as an integer
    """

    wc = textstat.lexicon_count(infile)
    
    return wc

def readability(infile):
    """ readability stats 

    :infile: a file object; 
    :returns: Flesch index and Wiener sachtextformel index as floats
    """
    
    flesch = textstat.flesch_reading_ease(infile)
    stf = textstat.wiener_sachtextformel(infile, 1)

    return flesch, stf

if __name__ == "__main__":
    infile = MainDoc("testdata/testtext2.md").docgen()
    print(wordcount(infile))
    print(readability(infile))
