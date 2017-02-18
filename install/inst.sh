#!/bin/sh
#execute script as root/sudo-user
sudo sh connector.sh
sudo sh converter.sh
sudo sh seperator.sh
sudo sh ubuntu.sh
connectorPath=""
while read "connector"; 
do 
 connectorPath=$connector 
 sudo chmod -R 777 $connector
done < tmpConnector.txt

converterPath=""
converterFile="/convertToTxt.py"
while read "converter"; 
do 
 converterPath=$converter$converterFile 
 sudo chmod -R 777 $converter
done < tmpConverter.txt

seperatorPath=""
checkerPath=""
seperatorFile="/seperator.py"
checkerFile="/checker.py"
while read "seperator"; 
do 
 seperatorPath=$seperator$seperatorFile 
 checkerPath=$seperator$checkerFile 
 sudo chmod -R 777 $seperator
done < tmpSeperator.txt

file="/path.cfg"
path=""
while read "main";
do 
 path=$main$file 
 sudo chmod -R 777 $main
done < tmpMain.txt

echo "[PFAD]" > $path
echo "converter="$converterPath >>$path
echo "checker="$checkerPath >>$path
echo "seperator="$seperatorPath >>$path

rm -r tmpConnector.txt tmpConverter.txt tmpSeperator.txt tmpMain.txt
