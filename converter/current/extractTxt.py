#!/usr/bin/python3
# -*- coding: utf-8 -*-
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
import loggingModule

def process(path):

    if(os.path.isfile(path)):
        loggingModule.logger3.debug('Started text extract')
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
        loggingModule.logger3.debug('End text extract')
        if extension[-1] != "rtf":
            try:
                encodedText = text.decode('utf-8', "strict")
            except Exception as e:
                loggingModule.logger3.error("Error: " + str(e))
                sys.exit(2)
        else:
            rtfString = text.decode("windows-1252")
            encodedText = rtfString.split('-' * 17 + '\n', 1)[-1]
        return encodedText
    else:
        loggingModule.logger3.warning("File not exist: error \n")
        sys.exit(1)


def file(text, a):
    if text is not None and a is not None:
        try:
            text_file = open(a, "w+")
            text_file.write(text)
            text_file.close()
        except Exception as e:
            loggingModule.logger3.error("Cannot write to file:" + str(e))
    else:
        loggingModule.logger3.error('Correct use: convertToTxt.py -p <PATH> -o <OUTPUTPATH>')
        sys.exit(2)
