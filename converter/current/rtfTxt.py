""" Modul zur Umwandlung von einer .rtf zu einer .txt """
import subprocess
import logging


def rtf_txt(filename):
    try:
        process = subprocess.Poen(["unrtf", "--text", filename], stdout=subprocess.PIPE)
        process.wait()
        text = process.stdout.read()
        #the 'split' deletes the unnessasary head information from the textfile
        return str(text,'utf-8').split('-'*17+'\n', 1)[-1]
    except:
        logging.error("filed to process " + filename)
    

