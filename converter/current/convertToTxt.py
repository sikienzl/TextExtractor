#!/usr/bin/python3
"""Converts any files into txt-files"""

from docTxt import *
from pdfTxt import *
import sys

class Converter:
	def __init__(self):
		pass

	def main():
		path = sys.argv[1]		
		#path = '/home/siegfried/python/converter/endungen/doc_example.doc'
		filename, extension = path.split(".")
		if extension == "doc":
			text = docTxt(path)
		if extension == "pdf":
			text = pdfTxt(path)
		print(text)
			

	if __name__ =='__main__':main()
