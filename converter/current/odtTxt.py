#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Modul zur Extrahierung von Text aus einer .odt-Datei """

import subprocess
import loggingModule


def odt_txt(filename):
    stderr = None
    try:
        process = subprocess.Popen(
            ['odt2txt', filename],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        text = process.stdout.read()
        process.stdout.close()
        return text
    except Exception as e:
        loggingModule.logger6.error(e)
