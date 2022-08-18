#!/bin/sh
if [ ! -f "/usr/bin/pip3" ] ; then
	apt-get -y install python3-pip
fi
pip3 install -U nltk
#/usr/bin/python3 -m nltk.downloader -d /usr/share/nltk_data punkt
pathTar="seperator.tar"

while true
   do
	path=`dialog --inputbox "Where should the seperator scripts be installed?" 0 0 3>&1 1>&2 2>&3`
	respose=$?
	case $respose in
	  0)

	if [ ! -d $path ] ; then
		dialog --title "Create Path" --yesno "Should path be created?" 15 60
		antwort=$?
		case $antwort in
			0)
				dialog --backtitle "Path" --title "Create" --msgbox "Path is created!" 15 40
				touch tmpSeperator.txt
				echo $path > tmpSeperator.txt
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

