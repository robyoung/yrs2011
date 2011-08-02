import nltk.data
from nltk.tokenize import RegexpTokenizer
import sys
import os
import pickle

path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data/classifiers/%s.pickle" % sys.argv[1])
classifier = pickle.load(open(path))

print classifier.classify(dict((word, True) for word in RegexpTokenizer(r"[\w']+").tokenize(sys.argv[2])))