#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""loggingModule.py: creates the logger for the different python modules"""

__author__ = "Mark Unger, Siegfried Kienzle"

import logging
import logging.handlers
import os
import errno

LOG_FILE = os.path.abspath(os.path.dirname(__file__)) + "/logging.log"

# logger for console and file with maxbyte=1mb
logging.getLogger().setLevel(logging.INFO)

logger1 = logging.getLogger('separator.py')
logger2 = logging.getLogger('checker.py')

formatter = logging.Formatter('%(message)s')

# console
console = logging.StreamHandler()
console.setFormatter(formatter)
console.setLevel(logging.INFO)

# file
filehandler = logging.FileHandler(LOG_FILE)
file_formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
filehandler = logging.handlers.RotatingFileHandler(
    LOG_FILE,
    mode='a',
    maxBytes=1000000,
    backupCount=1)
filehandler.setFormatter(file_formatter)
filehandler.setLevel(logging.WARNING)

logger1.addHandler(console)
logger1.addHandler(filehandler)
logger2.addHandler(console)
logger2.addHandler(filehandler)
