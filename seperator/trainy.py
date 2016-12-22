#!/usr/bin/python3 -w

import nltk.tokenize.punkt
import pickle
import codecs
tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
text = codecs.open("master_bp.txt", "r", "utf8").read()
tokenizer.train(text)
out = open("business.pickle", "wb")
pickle.dump(tokenizer, out)
out.close()
