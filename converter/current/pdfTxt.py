""" Modul zur Extrahierung von Text aus einer .pdf-Datei """

import subprocess


def pdf_txt(filename):
    try:
        process = subprocess.Popen(
            ["pdftotext", filename, '-'], stdout=subprocess.PIPE)
        process.wait()
        return process.stdout.read()

    except:
        logging.error("filed to process " + filename)
