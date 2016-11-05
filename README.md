# Teamprojekt
-------------
## alte Vorgehensweise
----------------------
### Implementierungen
---------------------
- Main-File "convertToTxt" implementiert
- Modul "docTxt" implementiert
- Modul "docxTxt" implementiert
- Modul "pdfTxt" implementiert
- Modul "rtfTxt" implementiert
- Modul "odtTxt" implementiert

### benötigte Installationen
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

### Überlegungen
---------------
- Überlegung für das Modul "docxTxt":
  http://www.commandlinefu.com/commands/view/4311/extract-plain-text-from-ms-word-docx-files
  --> getestet in Konsole: :heavy_check_mark:
- Formatieren mit autopep8

## neue Vorgehensweise
----------------------
### Implementierungen
--------------------
- arbeiten mit Modul "textract"

#### benötige Installationen
----------------------------
- werden folgende Pakete benötigt; Installation unter debian/ubuntu:

    ```apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr
flac ffmpeg lame libmad0 libsox-fmt-mp3 sox```

```pip install textract```

Muss bug gefixt werden für python3, wenn man ```pip3 install textract``` macht.

How to install textract for python3: http://www.tysonmaly.com/installing-textract-for-python-3/

Fehler bei ```pip install textract``` auf Ubuntu 14.04.05-LTS VM: 
ValueError: jpeg is required unless explicitly disabled using --disable-jpeg, aborting.

Lösung:
```apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk```

### Überlegungen
----------------
- Verwendung dieser Bibliothek
- Wechseln wieder zu Vorgehensweise 1

## Installationskript
---------------------

### TODO-Liste
--------------
- Prüfung auf python-docx2txt fehlt, da die Installation über ```pip3 install doc2txt``` und ```easy_install3 doc2txt``` erfolgt
- Kommentare fehlen
- an einigen Stellen fehlt eine Fehlerbehandlung
- Finally: Funktionstest ob alle Abhängigkeiten abgedeckt wurden
