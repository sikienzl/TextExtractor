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
        text = select_textextension_type(extension, path)
        loggingModule.logger3.debug('End text extract')
        if extension[-1] != "rtf":
            try:
                encoded_text = text.decode('utf-8', "strict")
            except Exception as e:
                loggingModule.logger3.error("Error 1: " + str(e) + " on path:" + str(path))
                sys.exit(2)
        else:
            rtf_string = text.decode("windows-1252")
            encoded_text = rtf_string.split('-' * 17 + '\n', 1)[-1] 
        return encoded_text
    else:
        loggingModule.logger3.warning("Warning 1: File not exist: error \n")
        sys.exit(1)

def select_textextension_type(extension, path):
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
    return text

def file(text, a):
    if text is not None and a is not None:
        try:
            text_file = open(a, "w+")
            text_file.write(text)
            text_file.close()
        except Exception as e:
            loggingModule.logger3.error("Error 2:" + str(e))
    else:
        loggingModule.logger3.error('Correct use: convertToTxt.py -p <PATH> -o <OUTPUTPATH>')
        sys.exit(2)
