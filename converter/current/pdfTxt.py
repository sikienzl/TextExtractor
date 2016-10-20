""" Modul zur Umwandlung von einer .pdf zu einer .txt """

import subprocess 


def pdf_txt(filename):
    process = subprocess.Popen(["pdftotext", filename,'-'], stdout=subprocess.PIPE)
    process.wait()
    return process.stdout.read()
