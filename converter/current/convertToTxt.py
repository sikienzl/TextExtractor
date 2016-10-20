#!/usr/bin/python3
"""Converts any files into txt-files"""

import docTxt
import pdfTxt
import sys


class Converter:
    def __init__(self):
        pass

    def main(self):
        path = sys.argv[1]
        #path = '/home/siegfried/python/converter/endungen/doc_example.doc'
        filename, extension = path.split(".")
        if extension == "doc":
            text = docTxt.doc_txt(path)
        if extension == "pdf":
            text = pdfTxt.pdf_txt(path)
            print(text)

    if __name__ == '__main__':
        main()
