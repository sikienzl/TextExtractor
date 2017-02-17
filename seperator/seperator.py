#!/usr/bin/python3

"""
separator.py:
separates the senteces in a file.
"""

__author__      = "Mark Unger, Siegfried Kienzle"


import sys
import getopt
# from nltk import data
import nltk.data
import loggingModule

# PICKLE_FILE = 'tokenizers/punkt/german.pickle'
PICKLE_FILE = 'business.pickle'


def main():
    argv = sys.argv[1:]
    string = None
    if(len(sys.argv) == 1):
        loggingModule.logger1.info("Please put a correct parameter!\n")
        loggingModule.logger1.info(help())
        
    try:
        opts, args = getopt.getopt(
            argv, "hvi:o:", ['help', 'input=', 'output='])
    except getopt.GetoptError as e:
         loggingModule.logger1.info("Please put a correct parameter!\n")

    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
             loggingModule.logger1.info(help())
        elif o in ("-i", "--input"):
            string = seperator(a)
        elif o in ("-o", "--output"):
            writeIntoFile(a, string)
        else:
             loggingModule.logger1.info(help())
    if verbose:
        if string is not None:
             loggingModule.logger1.info(string)
        else:
             loggingModule.logger1.info(help())


def seperator(filename):
    tokenizer = nltk.data.load(PICKLE_FILE)
    try:
        fp = open(filename)
        data = fp.read()
        tokenizerString = tokenizer.tokenize(data)
        # print(tokenizerString)
        tmpstr = "\n-----\n"
        # string = '\n'
        string = tmpstr.join(tokenizer.tokenize(data))
        return string
    except Exception as e:
        loggingModule.logger1.error("Error: " + str(e))


def writeIntoFile(filename2, string):
    if string:
        try:
            fh = open(filename2, 'w+')
            fh.write(string)
            fh.close()
        except IOError:
             loggingModule.logger1.error("Error occured when trying to write in file")


def help():
    return("arguments\n" +
           "-h,                      --help                          " +
           "show help message and exit\n" +
           "-i [path to file]        --input  [path to file]         " +
           "to run the program\n" +
           "-o [path to outputfile]  --output [path to outputfile]   " +
           "to extract text into file\n" +
           "-v                                                       " +
           "verbose-Mode")

if __name__ == '__main__':
    main()
