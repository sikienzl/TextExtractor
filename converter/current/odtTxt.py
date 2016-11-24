""" Modul zur Extrahierung von Text aus einer .odt-Datei """

import subprocess
import logging


def odt_txt(filename):
    stderr = None
    try:
        process = subprocess.Popen(
            ['odt2txt', filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        text = process.stdout.read()
        process.stdout.close()
        return text
    except Exception as e:
        logging.error(e)
        #logging.error(stderr)
