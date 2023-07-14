# TextExtractor  
-------------
[![CodeQL](https://github.com/sikienzl/TextExtractor/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/sikienzl/TextExtractor/actions/workflows/codeql-analysis.yml)

This project contains python-modules to
  * extract text from different formats (\*\.doc, \*\.docx, \*\.odt, \*\.pdf, \*\.rtf) 
  * removes header and footer
  * seperate sentences

It contains setup-files for the server distribution of ubuntu and the python-version 3.4.3.

If you would like to install these files, you go into the folder install and type ```./inst.sh```.

The seperator-module use the [Natural Language Toolkit](http://www.nltk.org/) and is distributed under the terms of the Apache License Version 2.0.

We refer to the following book:

*Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.*

The docx-module of the converter use [docx2txt](http://docx2txt.sourceforge.net/) and is distributed under the terms of the GPLv3.

## Tested
The following table shows you on which ubuntu versions the project is tested:

| Version | Tested | 
| ------- | ------ |
| 16.04 Server   | :heavy_check_mark: |
| 18.04 Server   | :heavy_check_mark: |
| 20.04 Server   | :heavy_check_mark: |
