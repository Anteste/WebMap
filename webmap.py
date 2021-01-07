#!/usr/bin/python3

import os
import sys
import socket
import string

ans = True

installed = True if os.path.exists("/bin/webmap") else False

def reopen():
    if installed:
        os.system("sudo webapp")

    else:
        os.system("sudo python3 webmap.py")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_dir(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)
while ans:
    print("====================================")
    print("#             WEBMAP               #")
    print("====================================")
    print("1. Nmap Scan")
    print("2. Dirsearch Scan")
    print("3. Nikto Scan")
    print("A. All the Scans")
    print("E. Exit")
    print("====================================")
    ans = input("What would you like to do? Enter your selection: ").upper()

    if ans == "1":
        clear()
        ans = True
        while ans:
            print("====================================")
            print("#             Nmap Scan            #")
            print("====================================")
            print("1. Scan An IP Address For Open Ports")
            print("2. Operating System Scan")
            print("3. Agressive Scan For An IP Address")
            print("4. Scan The Network For All Devices")
            print("M. Main Menu")
            print("====================================")
            ans = input("What would you like to do? Enter your selection: ")

            if ans == "1":
                clear()
                print("______________________________________________________________________")
                portscan = input("Enter the IP you want to scan the ports of: ")
                portipscan = socket.gethostbyname(portscan)
                print("______________________________________________________________________")
                os.system("nmap " + portipscan)
                print("______________________________________________________________________")

            elif ans == "2":
                clear()
                print("______________________________________________________________________")
                osscan = input("Enter the IP you want to find the operating system of: ")
                osipscan = socket.gethostbyname(osscan)
                print("______________________________________________________________________")
                os.system("nmap -O " + osipscan)
                print("______________________________________________________________________")

            elif ans == "3":
                clear()
                print("______________________________________________________________________")
                ascan = input("Enter the IP you want to scan: ")
                aipscan = socket.gethostbyname(ascan)
                print("______________________________________________________________________")
                os.system("nmap -A " + aipscan)
                print("______________________________________________________________________")

            elif ans == "4":
                clear()
                print("______________________________________________________________________")
                snscan = input("Enter your address and range (i.e. 192.168.0.1/24) now: ")
                snipscan = socket.gethostbyname(snscan)
                print("______________________________________________________________________")
                os.system("nmap -sn " + snipscan)
                print("______________________________________________________________________")

            elif ans == "M":
                clear()
                reopen()

            else:
                clear()
                print("Not Valid Choice Try again")
                reopen()
                ans = None

    elif ans == "2":
        clear()
        print("====================================")
        print("#        Dirsearch Scan            #")
        print("====================================")
        dirtarget = input("Enter target: ")
        print("______________________________________________________________________")
        os.system("/opt/dirsearch/dirsearch.py -u " + dirtarget)
        print("______________________________________________________________________")
        if ans == "":
            clear()

    elif ans == "3":
        clear()
        print("====================================")
        print("#            Nikto Scan            #")
        print("====================================")
        niktotarget = input("Enter target: ")
        print("______________________________________________________________________")
        os.system("nikto -host " + niktotarget)
        print("______________________________________________________________________")
        if ans == "":
            clear()

    elif ans == "A":
        clear()
        print("====================================")
        print("#         All The Scans            #")
        print("====================================")
        targetall = input("Enter the target URL : ")
        ipall = socket.gethostbyname(targetall)
        print("___________________________________________________________________________")
        targetOutput = "reports/" + targetall
        create_dir(targetOutput)
        os.system(
            'gnome-terminal -- bash -c "nmap -A '
            + ipall
            + " -o "
            + targetOutput
            + '/nmap.txt && bash"'
        )
        os.system(
            'gnome-terminal -- bash -c "python3 /opt/dirsearch/dirsearch.py -u '
            + targetall
            + " --simple-report="
            + targetOutput
            + '/dirsearch.txt && bash"'
        )
        os.system(
            'gnome-terminal -- bash -c "nikto +h '
            + targetall
            + " -output "
            + targetOutput
            + '/nikto.txt && bash"'
        )
        if ans == "":
            clear()

    elif ans == "E":
        clear()
        ans = None
    else:
        clear()
        print("Not Valid Choice Try again")
        reopen()