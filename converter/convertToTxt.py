#!/usr/bin/python3
"""Converts any files into txt-files"""

from docTxt import *

class Converter:
	def __init__(self):
		pass

	def main():
		path = '/home/siegfried/python/converter/endungen/doc_example.doc'
		filename, extension = path.split(".")
		if extension == "doc":
			txt = docTxt('/home/siegfried/python/converter/endungen/doc_example.doc')
			print(txt)

	if __name__ =='__main__':main()
