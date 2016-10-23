""" Modul zur Extrahierung von Text aus einer .docx-Datei """

import subprocess


def docx_txt(filename):
    stderr = None
    try:
        process = subprocess.Popen(["unzip", "-p", filename,"word/document.xml"], 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.wait()
        return process.stdout.read()
    
    except:
        logging.error(stderr)
	#logging.error("filed to process " + filename)
