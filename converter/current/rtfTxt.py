#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Modul zur Extrahierung von Text aus einer .rtf-Datei """
import subprocess
import loggingModule


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
        loggingModule.logger8.error(e)
