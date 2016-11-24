""" Modul zur Extrahierung von Text aus einer .rtf-Datei """
import subprocess
import logging


def rtf_txt(filename):
    try:
        process = subprocess.Popen(
            ["unrtf", "--text", filename], stdout=subprocess.PIPE)
        process.wait()
        text = process.stdout.read()
        process.stdout.close()
        # the 'split' deletes the unnessasary head information from the
        # textfile
        rtfString = str(text, 'utf-8').split('-' * 17 + '\n', 1)[-1]
        return rtfString.encode()
    except Exception as e:
        logging.error(e)
        #logging.error("filed to process " + filename)
