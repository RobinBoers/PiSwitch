#!/bin/bash

python /opt/retropie/configs/all/NewTouchBoot/selection.py

source /opt/retropie/configs/all/NewTouchBoot/checknum

if [ $num -eq 1 ]
then
     sleep 2
     emulationstation
elif [ $num -eq 2 ]
then
     kodi
elif [ $num -eq 3 ]
then
     sleep 2
     startx
elif [ $num -eq 4 ]
then
     exit 0
elif [ $num -eq 5 ]
then
     sleep 2
     emulationstation
fi
