# Teamprojekt
-------------
## alte Vorgehensweise
----------------------
### Implementierungen
--------------------
- Main-File "convertToTxt" implementiert
- Modul "docTxt" implementiert
- Modul "docxTxt" angefangen zu implementieren

### benötigte Installationen
---------------------------
- wird das Paket catdoc benötigt; Installation unter debian/ubuntu:
    ```apt-get install catdoc```
- Für PDF das Paket pdftotext installieren:
    ```apt-get install pdftotext```

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

Muss bug gefixt werden für python3, wenn man pip3 install textract macht.

How to install textract for python3: http://www.tysonmaly.com/installing-textract-for-python-3/

### Überlegungen
----------------
- Verwendung dieser Bibliothek
