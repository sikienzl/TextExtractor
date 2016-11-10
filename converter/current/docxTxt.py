""" Modul zur Extrahierung von Text einer .docx-Datei"""

import docx2txt
import logging


def docx_txt(filename):
    stderr = None
    try:
        text = docx2txt.process(filename)
        return text.encode()
    except:
        logging.error(stderr)
        #logging.error("filed to process " + filename)
