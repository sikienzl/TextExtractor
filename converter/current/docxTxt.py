""" Modul zur Extrahierung von Text aus einer .docx-Datei """

import subprocess


def docx_txt(filename):
    try:
        process = subprocess.Popen(["unzip", "-p", filename,"word/document.xml"], stdout=subprocess.PIPE)
        process.wait()
        return process.stdout.read()
    
    except:
        logging.error("filed to process " + filename)
