#!/usr/bin/bash

# Verify the OS witch is using and install on the right one
if [ "$(grep -Ei 'debian|buntu|mint' /etc/*release)" ]; then ##If need more distributions just add more
    sudo apt-get install nmap nikto git -y
elif [ "$(grep -Ei 'redhat|centos' /etc/*release)" ]; then ##To install on RPM CentOS/RedHat
    os_version=`cat /etc/system-release-cpe | cut -d ':' -f5`
    if [ $os_version == 8 ]; then
        sudo dnf install https://extras.getpagespeed.com/release-el8-latest.rpm -y
        sudo dnf install nikto nmap -y 
    elif [ $os_version == 7 ]; then
        sudo rpm -Uvh http://www6.atomicorp.com/channels/atomic/centos/7/x86_64/RPMS/atomic-release-1.0-20.el7.art.noarch.rpm
        sudo rpm  -Uvh http://www6.atomicorp.com/channels/atomic/centos/7/x86_64/RPMS/atomic-release-1.0-21.art.noarch.rpm
        sudo rpm -Uvh  http://www6.atomicorp.com/channels/atomic/centos/7/x86_64/RPMS/atomic-release-1.0-21.art.noarch.rpm 
        sudo yum install nikto nmap git -y  
    fi
fi   

pip3 install -r conf/requirements.txt
sudo chmod +x webmap.py
sudo ln -s webmap.py webmap
cd /opt && sudo git clone https://github.com/maurosoria/dirsearch.git
cd -
