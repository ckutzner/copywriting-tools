""" module for stats """
import textstat

def wordcount(infile):
    """ count words

    :infile: a text file 
    :returns: wordcount as an integer
    """
    
    with open(infile) as file:
        text = file.read()

    wc = textstat.lexicon_count(text)
    
    return wc

def readability(infile):
    """ readability stats 

    :infile: a text file; 
    :returns: Flesch index and Wiener sachtextformel index as floats
    """
    
    with open(infile) as file:
        text = file.read()
    
    flesch = textstat.flesch_reading_ease(text)
    stf = textstat.wiener_sachtextformel(text, 1)

    return flesch, stf
