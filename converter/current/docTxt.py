""" Modul zur Umwandlung von einer .doc zu einer .txt """

import subprocess 


def doc_txt(filename):
    process = subprocess.Popen(['catdoc','-w', filename], stdout=subprocess.PIPE)
    process.wait()
    return process.stdout.read()