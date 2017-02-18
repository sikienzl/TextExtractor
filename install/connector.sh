#!/bin/sh

# Check if files not exist (-f)
if [ ! -f "/usr/bin/dialog" ] ; then
	apt-get -y install dialog 
fi

if [ ! -f "/usr/bin/pv" ] ; then
	apt-get -y install pv
fi

#includes all python-scripts
pathTar="connector.tar"

while true
   do
	path=`dialog --inputbox "Wohin sollen die Connector-Scripts installiert werden?" 0 0 3>&1 1>&2 2>&3`
	respose=$?
	case $respose in
	  0)
	# Check if path not exist
	if [ ! -d $path ] ; then
		dialog --title "Create Path" --yesno "Soll Pfad erstellt werden?" 15 60 
		antwort=$?
		case $antwort in
			0) 
				dialog --backtitle Pfad --title Erstellen --msgbox "Pfad wird erstellt!" 15 40
				touch ./tmpConnector.txt
				echo $path > tmpConnector.txt
				mkdir $path
				;;
			1) continue;;
		esac
	fi
	# Check if Destination-Path-Variable not empty
	if [ -n "$path" ] ; then 
		# Extract moduls.tar into Destination-Path
		#dialog --backtitle InfoExtract --title Entpacken --msgbox "Die python-Dateien werden nun entpackt!" 15 40
		#tar xfv $pathTar -C $path
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
