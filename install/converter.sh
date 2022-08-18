#!/bin/sh

# Check if files not exist (-f)
if [ ! -f "/usr/bin/dialog" ] ; then
	apt-get -y install dialog 
fi

if [ ! -f "/usr/bin/pv" ] ; then
	apt-get -y install pv
fi

if [ ! -f "/usr/bin/catdoc" ] ; then
	apt-get -y install catdoc
fi

if [ ! -f "/usr/bin/unrtf" ] ; then
	apt-get -y install unrtf
fi

if [ ! -f "/usr/bin/odt2txt" ] ; then
	apt-get -y install odt2txt
fi

if [ ! -f "/usr/bin/pdftotext" ] ; then
	apt-get -y install poppler-utils
fi

if [ ! -f "/usr/bin/easy_install3" ] ; then
	apt-get -y install python3-setuptools
fi

#checks if python-modul is installed and write the error into numpy_check
docx2txt_check=$(python3 -c "import docx2txt" 2>&1)

if [ -n "$docx2txt_check" ] ; then
	pip3 install docx2txt
	easy_install3 docx2txt
fi



#includes all python-scripts
pathTar="converter.tar"

while true
   do
	path=`dialog --inputbox "Where should the converter scripts be installed?" 0 0 3>&1 1>&2 2>&3`
	respose=$?
	case $respose in
	  0)
	# Check if path not exist
	if [ ! -d $path ] ; then
		dialog --title "Create Path" --yesno "Should the path be created?" 15 60 
		antwort=$?
		case $antwort in
			0) 
				dialog --backtitle "Path" --title "Create" --msgbox "Path is created!" 15 40
				touch tmpConverter.txt
				echo $path > tmpConverter.txt
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
