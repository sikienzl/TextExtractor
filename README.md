# Teamprojekt
-------------
## Connector
--------------------
### Beispiele
-------------
https://lempstacker.com/tw/Using-PyMySQL-as-MariaDB-Driver-for-Python3/

## Satztrennung
---------------
### Vorgehensweise
------------------
#### benötigte Installationen
-----------------------------

sudo pip3 install -U nltk

import nltk

nltk.download()

Dann auf "Download" und dann "punkt" eintippen. siehe:
http://stackoverflow.com/questions/4867197/failed-loading-english-pickle-with-nltk-data-load

Nun noch das gewünschte Buch in das Verzeichnis "/usr/share/nltk_data" downloaden:

```sudo /usr/bin/python3 -m nltk.downloader -d /usr/share/nltk_data punkt```

weitere Infos unter:

http://www.nltk.org/data

## Beispiel für Satztrennung
----------------------------

http://stackoverflow.com/questions/4576077/python-split-text-on-sentences

## Textextrahierung
-------------------
### Vorgehensweise
----------------------
#### Implementierungen
---------------------
- Main-File "convertToTxt" implementiert
- Modul "docTxt" implementiert
- Modul "docxTxt" implementiert
- Modul "pdfTxt" implementiert
- Modul "rtfTxt" implementiert
- Modul "odtTxt" implementiert

#### benötigte Installationen
----------------------------
- wird das Paket catdoc benötigt; Installation unter debian/ubuntu:
    ```apt-get install catdoc```
- Für PDF das Paket "poppler-utils" installieren:
    ```apt-get install poppler-utils```
- Für RTF das Paket "unrtf" installieren:
    ```apt-get install unrtf```
- Für odt das Paket "odt2txt" installieren:
    ```apt-get install odt2txt```
    
- Probleme beim Installieren von lxml, Lösung:

    ```apt-get install python3-setuptools```
    
    ```apt-get install libxml2-dev libxslt1-dev```
    
    ```apt-get install libxslt-dev```
    
    ```apt-get install python3-dev```
    
    ```easy_install3 lxml```

- Verwendung von python-docx2txt, Installation wie folgt:

    ```pip3 install docx2txt```
    
    ```easy_install3 docx2txt```
    
#### Problemlösungen
-------------------
Beispiel-Fehler:

```bash: ./inst.sh : /bin/sh^M: Defekter Interpreter: Datei oder Verzeichnis nicht gefunden```

Lösung:

--> dos2unix

#### TESTS
---------

##### Funktionstest
----------------

###### Pythonmodule:
-------------------

docTxt.py :heavy_check_mark: :heavy_check_mark: 

docxTxt.py :heavy_check_mark: :heavy_check_mark:

pdfTxt.py :heavy_check_mark: :heavy_check_mark:

rtfTxt.py :heavy_check_mark: :heavy_check_mark:

odtTxt.py :heavy_check_mark: :heavy_check_mark:

#### Überlegungen
---------------
- Überlegung für das Modul "docxTxt":
  http://www.commandlinefu.com/commands/view/4311/extract-plain-text-from-ms-word-docx-files
  --> getestet in Konsole: :heavy_check_mark:
- Formatieren mit autopep8
- Wohin soll Text geschrieben werden?
- Bild-Text-Erkennung?
- eventuelle automatisierte Tests anfertigen?
- Exceptions eventuell anpassen?


### Installationskript
---------------------

#### TODO-Liste
--------------
- Prüfung auf python-docx2txt fehlt, da die Installation über ```pip3 install doc2txt``` und ```easy_install3 doc2txt``` erfolgt :heavy_check_mark:
- Kommentare fehlen
- an einigen Stellen fehlt eine Fehlerbehandlung
- convertToTxt.py fehlt noch die Abprüfung wenn ein falscher Parameter bzw. etwas falsches eingegeben wurde.
- Ausgabe umlenken in eine Datei. Vllt Option auf Konsole ausgeben beibehalten und aber dafür parameter einführen wo in *.txt-Datei schreibt.

#### Funktionstest
-----------------

inst.sh :heavy_check_mark: :heavy_check_mark:

ubuntu.sh :heavy_check_mark: :heavy_check_mark:
