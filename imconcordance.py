from bs4 import UnicodeDammit
import chardet
import os
import nltk
import codecs
import arabic_reshaper
import bidi.algorithm
import sys
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
import argparse
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-t", "--text", help="Text file to be processed")
args = vars(parser.parse_args())
def predict_encoding(file_path, n_lines=20):
    '''Predict a file's encoding using chardet'''
    import chardet

    # Open the file as binary data
    with open(file_path, 'rb') as f:
        # Join binary lines for specified number of lines
        rawdata = b''.join([f.readline() for _ in range(n_lines)])

    return chardet.detect(rawdata)['encoding']

text = args["text"]

def concordancing(text):
    with open(text, encoding = predict_encoding(text))as f:
        for f in f:
            tokens = nltk.word_tokenize(f)
            text = nltk.Text(tokens)
            text.concordance(input('what word u looking for:' ))
            print(text.concordance)
            bcf = BigramCollocationFinder.from_words(tokens)
            print(bcf.nbest(BigramAssocMeasures.likelihood_ratio, 4))
   # return()

concordancing(text)


