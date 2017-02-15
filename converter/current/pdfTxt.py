#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Modul zur Extrahierung von Text aus einer .pdf-Datei """

import subprocess
import loggingModule


def pdf_txt(filename):
    try:
        process = subprocess.Popen(
            ["pdftotext", "-layout", "-enc", "UTF-8",
             filename, '-'], stdout=subprocess.PIPE)
        text = process.stdout.read()
        process.stdout.close()
        return text

    except Exception as e:
        loggingModule.logger7.error(e)
