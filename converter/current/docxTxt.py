#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Modul zur Extrahierung von Text einer .docx-Datei """

import docx2txt
import loggingModule


def docx_txt(filename):
    text = ""
    try:
        text = docx2txt.process(filename)
        return text.encode()
    except AttributeError as aErr:
        loggingModule.logger5.error(aErr)
    except FileNotFoundError as fErr:
        loggingModule.logger5.error(fErr)
