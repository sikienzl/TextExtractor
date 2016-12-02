#!/bin/sh
pip3 install -U nltk
/usr/bin/python3 -m nltk.downloader -d /usr/share/nltk_data punkt
