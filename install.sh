#!/usr/bin/sh

sudo apt-get install gnome-terminal -y
sudo apt-get install nmap -y
sudo apt-get install nikto -y
sudo chmod +x webmap.py
sudo cp webmap.py /bin/webmap

