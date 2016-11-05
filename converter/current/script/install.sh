#!/bin/sh

if [ ! -f "/usr/bin/dialog" ] ; then
	apt-get install dialog
fi

if [ ! -f "/usr/bin/catdoc" ] ; then
	apt-get install catdoc
fi

if [ ! -f "/usr/bin/unrtf" ] ; then
	apt-get install unrtf
fi

if [ ! -f "/usr/bin/odt2txt" ] ; then
	apt-get install odt2txt
fi

if [ ! -f "/usr/bin/pdftotxt" ] ; then
	apt-get install poppler-utils
fi

pathTar="./moduls.tar"

while true
   do
	path=`dialog --inputbox "Wohin sollen die Python-Scripts installiert werden?" 0 0 3>&1 1>&2 2>&3`

	if [ ! -d $path ] ; then
		dialog --title "Create Path" --yesno "Soll Pfad erstellt werden?" 15 60 
		antwort=$?
		case $antwort in
			0) 
				dialog --backtitle Pfad --title Erstellen --msgbox "Pfad wird erstellt!" 15 40
				mkdir $path
				;;
			1) continue;;
		esac
	fi
	echo "$path"
	if [ -n "$path" ] ; then 
		tar xfv $pathTar -C $path
	fi
	break
  done
