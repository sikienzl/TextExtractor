#!/usr/bin/python3
"""Modul with logic"""

import docTxt
import docxTxt
import pdfTxt
import rtfTxt
import odtTxt
import sys
import getopt
import logging
import os.path

def process(path):
    if(os.path.isfile(path)):
        logging.info('Started text extract')
        extension = path.split(".")
        if extension[-1] == "doc":
            text = docTxt.doc_txt(path)
        if extension[-1] == "docx":
            text = docxTxt.docx_txt(path)
        if extension[-1] == "pdf":
            text = pdfTxt.pdf_txt(path)
        if extension[-1] == "rtf":
            text = rtfTxt.rtf_txt(path)
        if extension[-1] == "odt":
            text = odtTxt.odt_txt(path)
        logging.info('End text extract')
        encodedText = text.decode('utf-8')
        return encodedText
    else:
        logging.error('File not exist')
        print("File not exist: error \n") #+ help())
        sys.exit(1)

def file(text, a):
    if text != None and a != None:
        text_file=open(a,"w+")
        text_file.write(text)
        text_file.close()
    else:
        logging.error('Correct use: convertToTxt.py -p <PATH> -o <OUTPUTPATH>')
        print("Correct use: convertToTxt.py -p <PATH> -o <OUTPUTPATH>")
        sys.exit(2)
