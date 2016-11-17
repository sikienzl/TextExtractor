#!/usr/bin/python3
"""Converts any files into txt-files"""

import sys
import getopt
import logging
import os.path
import extractTxt

logFileName = 'logfile.log'

def main():
    argv = sys.argv[1:]
    text = None
    logging.basicConfig(filename=logFileName, level=logging.INFO,
                        format='%(asctime)s : %(levelname)s : %(message)s')
                        
    if(len(sys.argv) == 1):  # if no argument
        logging.info('No argument')
        print("Please put a correct parameter: error \n" + help())
    try:
        opts, args = getopt.getopt(argv, "hvp:o:", ['help', 'process=', 'output='])
    except getopt.GetoptError as e:
        logging.error(e)  # write into logfile
        logging.info(sys.argv[1] + " is not an argument")  # write into logfile
        print("Please put a correct parameter: error \n" + help())
        sys.exit(2)
    except:
        logging.error("Unexpected error")
        print("Unexpected error")

    if len(args) is not 0:
        logging.info(sys.argv[1] + " is not an argument")
        print("Please put a correct parameter: error \n" + help())
    
    verbose = False    
    text = None
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):  # help
            print(help())
        elif o in ("-p", "--process"):  # help
            text = extractTxt.process(a)
        elif o in ("-o", "--output"):
            extractTxt.file(text, a)
        else:
            logging.info('False argument')
            print("Please put a correct parameter: error \n" + help())
    if verbose == True:
       print(text)

def help():
    return("arguments:\n" +
           "-h, --help                                               show help message and exit\n" +
           "-p [path to file]        --process [path to file]        to run the program\n" +
           "-o [path to output-file] --output  [path to output-file] to extract text into file (works only with the argument -p)\n" +
           "-v                                                       verbose-Mode")

if __name__ == '__main__':
    main()
