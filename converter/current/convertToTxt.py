#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Converts any files into txt-files"""

import sys
import getopt
import logging
import os.path
import extractTxt
import loggingModule

def main():
    argv = sys.argv[1:]
    text = None

    if(len(sys.argv) == 1):  # if no argument
        loggingModule.logger2.info('No argument')
        loggingModule.logger2.info("Please put a correct parameter: error \n" + help())
    try:
        opts, args = getopt.getopt(
            argv, "hvi:o:", ['help', 'input=', 'output='])
    except getopt.GetoptError as e:
        loggingModule.logger2.error(e)  # write into logfile
        loggingModule.logger2.info(sys.argv[1] + " is not an argument")  # write into logfile
        loggingModule.logger2.info("Please put a correct parameter: error \n" + help())
        sys.exit(2)
    except:
        loggingModule.logger2.info("Unexpected error")

    if len(args) is not 0:
        logging.info(sys.argv[1] + " is not an argument")
        loggingModule.logger2.error("Please put a correct parameter: error \n" + help())

    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):  # help
            loggingModule.logger2.info(help())
        elif o in ("-i", "--input"):  # help
            text = extractTxt.process(a)
        elif o in ("-o", "--output"):
            extractTxt.file(text, a)
        else:
            loggingModule.logger2.info("Please put a correct parameter: error \n" + help())
    if verbose:
        if text is not None:
            loggingModule.logger2.info(text)
        else:
            loggingModule.logger2.info(help())


def help():
    return("arguments:\n" +
           "-h,                      --help                          " +
           "show help message and exit\n" +
           "-i [path to file]        --input [path to file]          " +
           "to run the program\n" +
           "-o [path to output-file] --output  [path to output-file] " +
           "to extract text into file \n" +
           "                                                         " +
           "(works only with the argument -i)\n" +
           "-v                                                       " +
           "verbose-Mode")

if __name__ == '__main__':
    main()
