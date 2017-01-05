""" Modul zur Extrahierung von Text aus einer .rtf-Datei """
import subprocess
import logging


def rtf_txt(filename):
    try:
        process = subprocess.Popen(
            ["unrtf", "--text", filename], stdout=subprocess.PIPE)
        text = process.stdout.read()
        # the 'split' deletes the unnessasary head information from the
        # textfile
        #rtfString = str(text, 'utf-8').split('-' * 17 + '\n', 1)[-1]
        return text
    except Exception as e:
        logging.error(e)
