#!/usr/bin/env bash
#
# Copyright (c) 2021 Iliass Alami Qammouri
#
# This is free software, licensed under the MIT License.
# See /LICENSE for more information.
#

DEPENDENCIES="nmap nikto git python3-pip"

# Verify the OS witch is using and install on the right one
if [ "$(grep -Ei 'debian|buntu|mint' /etc/*release)" ]; then ##If need more distributions just add more
    sudo apt-get install $DEPENDENCIES -y
elif [ "$(grep -Ei 'redhat|centos' /etc/*release)" ]; then ##To install on RPM CentOS/RedHat
    os_version=$(cut -d ':' -f5 < /etc/system-release-cpe)
    if [ "$os_version" == 8 ]; then
        sudo dnf install https://extras.getpagespeed.com/release-el8-latest.rpm -y
        sudo dnf install $DEPENDENCIES -y
    elif [ "$os_version" == 7 ]; then
        sudo rpm -Uvh http://www6.atomicorp.com/channels/atomic/centos/7/x86_64/RPMS/atomic-release-1.0-20.el7.art.noarch.rpm
        sudo rpm  -Uvh http://www6.atomicorp.com/channels/atomic/centos/7/x86_64/RPMS/atomic-release-1.0-21.art.noarch.rpm
        sudo rpm -Uvh  http://www6.atomicorp.com/channels/atomic/centos/7/x86_64/RPMS/atomic-release-1.0-21.art.noarch.rpm
        sudo yum install $DEPENDENCIES -y
    fi  
fi

pip3 install --user -r conf/requirements.txt
sudo ln -s "$(pwd)"/webmap.py /usr/local/bin/webmap
git clone --depth 1 https://github.com/maurosoria/dirsearch.git ~/.local/share/dirsearch