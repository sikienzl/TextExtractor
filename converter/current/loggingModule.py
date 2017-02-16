#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""loggingModule.py: creates the logger for the different python modules"""

__author__ = "Mark Unger, Siegfried Kienzle"

import logging
import logging.handlers
import os
import errno

# logger for console and file with maxbyte=1mb
logging.getLogger().setLevel(logging.INFO)

logger2 = logging.getLogger('convertToTxt.py')
logger3 = logging.getLogger('extractTxt.py')

logger4 = logging.getLogger('docTxt.py')
logger5 = logging.getLogger('docxTxt.py')
logger6 = logging.getLogger('odtTxt.py')
logger7 = logging.getLogger('pdfTxt.py')
logger8 = logging.getLogger('rtfTxt.py')

formatter = logging.Formatter('%(message)s')

# console
console = logging.StreamHandler()
console.setFormatter(formatter)
console.setLevel(logging.INFO)

# file
filehandler = logging.FileHandler("logging.log")
file_formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
filehandler = logging.handlers.RotatingFileHandler(
    "logging.log",
    mode='a',
    maxBytes=1000000,
    backupCount=1)
filehandler.setFormatter(file_formatter)
filehandler.setLevel(logging.WARNING)

logger2.addHandler(console)
logger2.addHandler(filehandler)
logger3.addHandler(console)
logger3.addHandler(filehandler)
logger4.addHandler(console)
logger4.addHandler(filehandler)
logger5.addHandler(console)
logger5.addHandler(filehandler)
logger6.addHandler(console)
logger6.addHandler(filehandler)
logger7.addHandler(console)
logger7.addHandler(filehandler)
logger8.addHandler(console)
logger8.addHandler(filehandler)
