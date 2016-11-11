""" Modul zur Extrahierung von Text einer .docx-Datei """

import docx2txt
import logging


def docx_txt(filename):
    text = ""
    try:
        text = docx2txt.process(filename)
        return text.encode()
    except AttributeError as aErr:
        logging.error(aErr)
    except FileNotFoundError as fErr:
        logging.error(fErr)
