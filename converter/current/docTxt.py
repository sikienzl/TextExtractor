#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Modul zur Extrahierung von Text aus einer .doc-Datei """

import subprocess
import loggingModule



def doc_txt(filename):
    stderr = None
    try:
        process = subprocess.Popen(
            ['catdoc', '-w', filename],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        text = process.stdout.read()
        process.stdout.close()
        return text
    except Exception as e:
        loggingModule.logger4.error(e)
