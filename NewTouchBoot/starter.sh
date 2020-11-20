#!/bin/bash

startx /opt/retropie/configs/all/NewTouchBoot/selection.py

source /opt/retropie/configs/all/NewTouchBoot/checknum

if [ $num -eq 1 ]
then
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
     emulationstation
fi
