#!/usr/bin/python3

import nltk.data

PICKLE_FILE = 'tokenizers/punkt/german.pickle'

def main():
	seperator("filename")

def seperator(filename):
	filename2 = "/home/siegfried/test.txt"
	tokenizer = nltk.data.load(PICKLE_FILE)
	fp = open(filename)
	data = fp.read()
	string = '\n'
	string.join(tokenizer.tokenize(data))
	writeIntoFile(filename2, string)	

def writeIntoFile(filename2, string):
	with open(filename2, 'a') as out:
		out.write(string)
	
	
def __name__ == "__main__":
	main()
