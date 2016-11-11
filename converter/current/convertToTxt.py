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


class Converter:

    def __init__(self):
        pass

    def main():
        text = None
        logging.basicConfig(filename=logFileName, level=logging.INFO,
                            format='%(asctime)s : %(levelname)s : %(message)s')
        logging.info('Started text extract')
        path = sys.argv[1]
        if(os.path.isfile(path)):
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
            print(encodedText)
        else:
            logging.error('File not exist')
        
    if __name__ == '__main__':
        main()
