""" Modul zur Umwandlung von einer .doc zu einer .txt """

import subprocess 


def doc_txt(filename):
    try:
        process = subprocess.Popen(['catdoc','-w', filename], stdout=subprocess.PIPE)
        process.wait()
        return process.stdout.read()
    
    except:
        logging.error("filed to process " + filename)
