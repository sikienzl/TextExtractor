'''Modul zum extrahieren von Text aus einer .odt-Datei'''

import subprocess
import logging

def odt_txt(filename):
        stderr = None
        try:
                process = subprocess.Popen(['odt2txt', filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.wait()
                return process.stdout.read()
        except:
                logging.error(stderr)

