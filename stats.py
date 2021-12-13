""" module for stats """
import textstat

def wordcount(infile):
    """ expects as input: a file; count total words in the text, return count as an integer"""
    file = open(infile)
    text = file.read()
    wc = textstat.lexicon_count(text)
    
    print("Text ist {} Worte lang.".format(wc))
    file.close()
    return wc

def readability(infile):
    """ expects as input: a file; returns Flesch index and Wiener sachtextformel index as floats"""
    file = open(infile)
    text = file.read()
    flesch = textstat.flesch_reading_ease(text)
    stf = textstat.wiener_sachtextformel(text, 1)

    print ("Flesch Index: {0:5.2f}\nWiener Sachtextformel: {1:5.2f}".format(flesch, stf))
    file.close()
    return flesch, stf
