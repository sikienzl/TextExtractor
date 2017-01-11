#!/bin/sh
pip3 install -U nltk
#/usr/bin/python3 -m nltk.downloader -d /usr/share/nltk_data punkt
pathTar="files.tar"

while true
   do
	path=`dialog --inputbox "Wohin sollen die Python-Scripte installiert werden?" 0 0 3>&1 1>&2 2>&3`
	respose=$?
	case $respose in
	  0)

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

	if [ -n "$path" ] ; then
		#{ tar -xfv $pathTar -C $path & }; dialog --infobox "Bitte warten Sie ..." 0 0; wait $!
		(pv -n $pathTar | tar xfv $pathTar -C $path ) 2>&1 | dialog --gauge "Extracting file..." 6 50
	else
		continue
	fi
	;;
	   1)
	break
	;;
	esac
	break
   done

