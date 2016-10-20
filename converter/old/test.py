#!/usr/bin/python3 -w

import textract
text = textract.process('/home/siegfried/python/sharedFolder/converter/new/endungen/pdf_example.pdf')
print(text)
