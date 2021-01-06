#!/usr/bin/bash

sudo apt-get install gnome-terminal -y
sudo apt-get install nmap -y
sudo apt-get install nikto -y
cd /opt && sudo git clone https://github.com/maurosoria/dirsearch.git
sudo chmod +x webmap.py
sudo cp webmap.py /bin/webmap

