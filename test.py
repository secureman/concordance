import nltk
import codecs
import arabic_reshaper
import bidi.algorithm
import sys
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
#nltk.download('punkt')
"""
raw  = The little pig saw the wolf climb up on the roof and lit a roaring fire in the fireplace and\
           placed on it a large kettle of water.When the wolf finally found the hole in the chimney he crawled down\
           and KERSPLASH right into that kettle of water and that was the end of his troubles with the big bad wolf.\
           The next day the little pig invited his mother over . She said &amp;amp;quot;You see it is just as I told you
           The way to get along in the world is to do things as well as you can.&amp;amp;quot; Fortunately for that litt
           he learned that lesson. And he just lived happily ever after!"""
##reshaped_text = arabic_reshaped.reshape(text)
##bidi_text = bidi.algorithm(reshaped_text)
def concordancing(text):
    with open(sys.argv[1], encoding = 'utf-8')as f:
        for f in f:
            tokens = nltk.word_tokenize(arabic_reshaper.reshape(f))
            text = nltk.Text(tokens)
            text.concordance(input('what word u looking for:' ))
            print(text.concordance)
            bcf = BigramCollocationFinder.from_words(tokens)
            print(bcf.nbest(BigramAssocMeasures.likelihood_ratio, 4))
    return()
print(concordancing(sys.argv[1]))
