""" Modul zur Umwandlung von einer .doc zu einer .txt """

import subprocess
import logging


def doc_txt(filename):
    stderr = None
    try:
        process = subprocess.Popen(
            ['catdoc', '-w', filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.wait()
        return process.stdout.read()
    except:
        logging.error(stderr)
        #logging.error("filed to process " + filename)
