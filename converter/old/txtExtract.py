#!/usr/bin/python3 -w

""" Modul zum extrahieren von Text aus saemtlichen Endungen """

import textract

def textract(pfad):
	text = textract.process(pfad)
	return text
