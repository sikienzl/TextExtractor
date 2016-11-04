""" Modul zur Umwandlung von einer .rtf zu einer .txt """
import subprocess
import logging


def rtf_txt(filename):
    try:
        process = subprocess.Popen(["unrtf", "--text", filename], stdout=subprocess.PIPE)
        process.wait()
        text = process.stdout.read()
        #the 'split' deletes the unnessasary head information from the textfile
        rtfString = str(text,'utf-8').split('-'*17+'\n', 1)[-1]
        return rtfString.encode()
    except:
        logging.error("filed to process " + filename)
