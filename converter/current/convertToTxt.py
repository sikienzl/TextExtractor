#!/usr/bin/python3
"""Converts any files into txt-files"""

import docTxt
import docxTxt
import pdfTxt
import rtfTxt
import odtTxt
import sys
import getopt
import logging
import os.path

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
        opts, args = getopt.getopt(argv, "hp:o:", ['help', 'process=', 'output='])
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
    
    for o, a in opts:
        if o in ("-h", "--help"):  # help
            print(help())
        elif o in ("-p", "--process"):  # help
            text = process(a)
            #text = process(sys.argv[2])
            print(text)
        elif o in ("-o", "--output"):
            file(text)
        else:
            logging.info('False argument')
            print("Please put a correct parameter: error \n" + help())

def process(path):
    if(os.path.isfile(path)):
        logging.info('Started text extract')
        filename, extension = path.split(".")
        if extension == "doc":
            text = docTxt.doc_txt(path)
        if extension == "docx":
            text = docxTxt.docx_txt(path)
        if extension == "pdf":
            text = pdfTxt.pdf_txt(path)
        if extension == "rtf":
            text = rtfTxt.rtf_txt(path)
        if extension == "odt":
            text = odtTxt.odt_txt(path)
        logging.info('End text extract')
        encodedText = text.decode('utf-8')
        return encodedText
    else:
        logging.error('File not exist')
        print("File not exist: error \n" + help())
        sys.exit(2)

def file(text):
    if text != None:
        print("hallo WELT")
    else:
        logging.error('Correct use: convertToTxt.py -p <PATH> -o <OUTPUTPATH>')
        print("Correct use: convertToTxt.py -p <PATH> -o <OUTPUTPATH>")

def help():
    return("arguments:\n" +
           "-h, --help                                      show help message and exit\n" +
           "-p [path to file]  --process [path to file]     to run the program")



if __name__ == '__main__':
    main()
