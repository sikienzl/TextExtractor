#!/usr/bin/python3
"""Read docx-file with catdoc"""

import os

def doc_to_text_catdoc(filename):
	(fi, fo, fe) = os.popen3('catdoc -w "%s"' % filename)
	fi.close()
	retval = fo.read()
	fo.close()
	fe.close()
	if not erroroutput:
		return retval
	else:
		raise OSError("Executing the command caused an error: %s" %erroroutput)
