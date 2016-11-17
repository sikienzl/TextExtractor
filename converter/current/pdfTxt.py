""" Modul zur Extrahierung von Text aus einer .pdf-Datei """

import subprocess


def pdf_txt(filename):
    try:
        process = subprocess.Popen(
            ["pdftotext", filename, '-'], stdout=subprocess.PIPE)
        text = process.stdout.read()
        process.stdout.close()
        return text

    except:
        logging.error("filed to process " + filename)
