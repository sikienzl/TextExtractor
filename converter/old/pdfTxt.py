""" Modul zur Umwandlung von einer .pdf zu einer .txt """

import subprocess 

def pdfTxt(filename):
	process = subprocess.Popen(['pdftotext', filename,'-'], stdout=subprocess.PIPE)
	process.wait()
	return process.stdout.read()
