#!/usr/bin/python3

import sys
import getopt
#from nltk import data
import nltk.data

#PICKLE_FILE = 'tokenizers/punkt/german.pickle'
PICKLE_FILE = 'business.pickle'

def main():
        argv = sys.argv[1:]
        string = None
        if(len(sys.argv) == 1):
            print("Please put a correct parameter!\n")
            print(help())
        try:
            opts, args = getopt.getopt(argv, "hvi:o:", ['help', 'input=', 'output='])
        except getopt.GetoptError as e:
            print("Please put a correct parameter!\n")
	
        verbose = False
        for o, a in opts:
            if o == "-v":
                verbose = True
            elif o in ("-h", "--help"):
                print(help())
            elif o in ("-i", "--input"):
                string = seperator(a)
            elif o in ("-o", "--output"):
                writeIntoFile(a, string)
            else:
                print(help())
        if verbose == True:
            if string != None:
                print(string)
            else:
                print(help())

def seperator(filename):
        tokenizer = nltk.data.load(PICKLE_FILE)
        fp = open(filename)
        data = fp.read()
        tmpstr = "\n-------\n"
        #string = '\n'
        string = tmpstr.join(tokenizer.tokenize(data))
        return string
        
def writeIntoFile(filename2, string):
        try:
            fh = open(filename2, 'w+')
            fh.write(string)
            fh.close()
        except IOError:
            print("fehler")
	
def help():
        return("arguments\n" +
           "-h,                      --help                          show help message and exit\n" +
           "-i [path to file]        --input  [path to file]         to run the program\n" +
           "-o [path to outputfile]  --output [path to outputfile]   to extract text into file\n" +
           "-v                                                       verbose-Mode")
	
if __name__ == '__main__' :
        main()
