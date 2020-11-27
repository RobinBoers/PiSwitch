#!/bin/bash

echo "Installing requierd packages"
sudo apt-get install -y python-wxgtk3.0
sudo apt-get install -y matchbox-keyboard

echo "Cloning repo..."
git clone  https://github.com/RobinBoers/PiSwitch /home/pi/PiSwitch

echo "Copying files..."
sudo cp /home/pi/PiSwitch/autostart.sh /opt/retropie/configs/all/autostart.sh
sudo cp -R /home/pi/PiSwitch/NewTouchBoot/ /opt/retropie/configs/all/NewTouchBoot

echo "Setting premissions"
sudo chmod 777 /opt/retropie/configs/all/NewTouchBoot/checknum
sudo chmod 777 /opt/retropie/configs/all/NewTouchBoot/retro.jpg
sudo chmod 777 /opt/retropie/configs/all/NewTouchBoot/kodi.jpg
sudo chmod 777 /opt/retropie/configs/all/NewTouchBoot/terminal.png
sudo chmod 777 /opt/retropie/configs/all/NewTouchBoot/Debian.jpg
sudo chmod 777 /opt/retropie/configs/all/NewTouchBoot/left.jpg
sudo chmod 777 /opt/retropie/configs/all/NewTouchBoot/right.jpg
sudo chmod 777 /opt/retropie/configs/all/NewTouchBoot/check.png
sudo chmod 777 /opt/retropie/configs/all/NewTouchBoot/logfile.txt
sudo chmod 777 /opt/retropie/configs/all/NewTouchBoot/starter.sh
sudo chmod a+x /opt/retropie/configs/all/NewTouchBoot/starter.sh
sudo chmod 777 /opt/retropie/configs/all/NewTouchBoot/selection.py
sudo chmod a+x /opt/retropie/configs/all/NewTouchBoot/selection.py
sudo chmod 777 /opt/retropie/configs/all/autostart.sh
sudo chmod a+x /opt/retropie/configs/all/autostart.sh

echo "Done. Rebooting now"
sudo reboot
