""" Modul zur Extrahierung von Text aus einer .docx-Datei """

import subprocess

def docxTxt(filename):
	process = subprocess.Popen(["unzip", "-p", filename,"word/document.xml"], stdout=subprocess.PIPE)
	process.wait()
	return process.stdout.read()
