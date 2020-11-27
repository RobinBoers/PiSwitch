# The PiSwitch boot screen as a standalone program

I'm making the PiSwitch boot screen into a standalone repo. I'm doing this mainly for personal use.

NewTouchBoot is a folder that gets put under `/opt/retropie/configs/all/`
It contains a bunch of scripts and a python program that launches a touch boot option menu.

## Installation
<code>
wget https://raw.githubusercontent.com/RobinBoers/PiSwitch/master/setup.sh<br>
sudo chmod 777 setup.sh && sudo chmod a+x setup.sh<br>
./setup.sh<br>
</code>