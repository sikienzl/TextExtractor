# -*- coding: utf-8 -*-
import logging
import logging.handlers
import os
import errno

#logger for console and file with maxbyte=1mb
logging.getLogger().setLevel(logging.INFO)

logger1 = logging.getLogger('separator.py')

formatter = logging.Formatter('%(message)s')

console = logging.StreamHandler()
console.setFormatter(formatter)
console.setLevel(logging.INFO)

filehandler = logging.FileHandler("logging.log")
file_formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
filehandler = logging.handlers.RotatingFileHandler("logging.log", mode='a',maxBytes=1000000, backupCount=1)
filehandler.setFormatter(file_formatter)
filehandler.setLevel(logging.WARNING)

logger1.addHandler(console)
logger1.addHandler(filehandler)
