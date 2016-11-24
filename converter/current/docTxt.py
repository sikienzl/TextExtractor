""" Modul zur Extrahierung von Text aus einer .doc-Datei """

import subprocess
import logging


def doc_txt(filename):
    stderr = None
    try:
        process = subprocess.Popen(
            ['catdoc', '-w', filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        text = process.stdout.read()
        process.stdout.close()
        return text
    except Exception as e:
        logging.error(e)
        #logging.error(stderr)
