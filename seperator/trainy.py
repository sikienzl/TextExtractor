#!/usr/bin/python3 -w

import nltk.tokenize.punkt
import pickle
import codecs
import sys
import getopt

tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()


def main():
    argv = sys.argv[1:]
    text = None
    if(len(sys.argv) == 1):
        print("Please put a correct parameter!\n")
        print(help())
    try:
        opts, args = getopt.getopt(
            argv, "hi:o:", ['help', 'input=', 'output='])
    except getopt.GetoptError as e:
        print("Please put a correct parameter!\n")
    for o, a in opts:
        if o in ("-h", "--help"):
            print(help())
        elif o in ("-i", "--input"):
            text = getText(a)
        elif o in ("-o", "--output"):
            if a is not None:
                writePickleFile(text, a)
            else:
                print("No filename for output-file\n")
        else:
            print(help())


def getText(filename):
    tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
    text = codecs.open(filename, "r", "utf8").read()
    return text


def writePickleFile(text, filename):
    tokenizer.train(text)
    out = open(filename, "wb")
    pickle.dump(tokenizer, out)
    out.close()


def help():
    return("arguments\n" +
           "-h,                        --help                              " +
           "show help message and exit\n" +
           "-i [path to file]          --input [path to file]              " +
           "read the input-file\n" +
           "-o [path to outputfile]    --output [path to outputfile]       " +
           "to write data into file\n")

if __name__ == "__main__":
    main()
