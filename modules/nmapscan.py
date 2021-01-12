#!/usr/bin/env python3
#
# Copyright (c) 2021 Iliass Alami Qammouri
#
# This is free software, licensed under the MIT License.
# See /LICENSE for more information.
#

import conf.conf as conf

def nmapScan() :    
    def tcpScanFunc() :
        conf.clear()

        print("______________________________________________________________________")
        
        tcpScan = input(conf.colored("\nEnter the IP you want to Scan the ports of: ", 'green', attrs=['bold']))
        tcpOutput = input(conf.colored(f"Enter the output folder - [default: reports/Nmap/{tcpScan}/]: ","green", attrs=['bold']))
        tcpIpScan = conf.socket.gethostbyname(tcpScan)

        conf.notValid(udpScanFunc,tcpScan)
        tcpOutput = conf.dirOutput(tcpOutput, "reports/Nmap/", tcpScan)
        conf.createDir(tcpOutput)
        
        print("______________________________________________________________________")
        
        conf.os.system(f"nmap -sS {tcpIpScan} -o {tcpOutput}/tcpscan.txt")
        
        print("______________________________________________________________________")

    def udpScanFunc() :        
        print("______________________________________________________________________")
        
        udpScan = input(conf.colored("\nEnter the IP you want to Scan the ports of: ", 'green', attrs=['bold']))
        udpOutput = input(conf.colored(f"Enter the output folder - [default: reports/Nmap/{udpScan}/]: ","green", attrs=['bold']))
        udpIpScan = conf.socket.gethostbyname(udpScan)

        conf.notValid(udpScanFunc,udpScan)
        udpOutput = conf.dirOutput(udpOutput, "reports/Nmap/", udpScan)
        conf.createDir(udpOutput)
     
        print("______________________________________________________________________")
        
        conf.os.system(f"sudo nmap -sU {udpIpScan} -o {udpOutput}/udpscan.txt")
        
        print("______________________________________________________________________")

    def osScanFunc() :
        print("______________________________________________________________________")
        
        osScan = input(conf.colored("\nEnter the IP you want to find the operating system of: ", 'green', attrs=['bold']))
        osOutput = input(conf.colored(f"Enter the output folder - [default: reports/Nmap/{osScan}/]: ","green", attrs=['bold']))
        osIpScan = conf.socket.gethostbyname(osScan)

        conf.notValid(osScanFunc,osScan)
        osOutput = conf.dirOutput(osOutput, "reports/Nmap/", osScan)
        conf.createDir(osOutput)
        
        print("______________________________________________________________________")
        
        conf.os.system(f"sudo nmap -O {osIpScan} -o {osOutput}/osscan.txt")
        
        print("______________________________________________________________________")

    def aScanFunc() :
        print("______________________________________________________________________")
        
        aScan = input(conf.colored("\nEnter the IP you want to Scan: ", 'green', attrs=['bold']))
        aOutput = input(conf.colored(f"Enter the output folder - [default: reports/Nmap/{aScan}/]: ","green", attrs=['bold']))            
        aIpScan = conf.socket.gethostbyname(aScan)

        conf.notValid(aScanFunc,aScan)
        aOutput = conf.dirOutput(aOutput, "reports/Nmap/", aScan)
        conf.createDir(aOutput)
        
        print("______________________________________________________________________")
        
        conf.os.system(f"sudo nmap -T4 -A {aIpScan} -o {aOutput}/ascan.txt")
        
        print("______________________________________________________________________")

    def netScanFunc() :
        conf.clear()
        
        print("______________________________________________________________________")
        
        snScan = input(conf.colored("\nEnter your address and range (i.e. 192.168.0.1/24) now: ", 'green', attrs=['bold']))
        snPrint = snScan.split("/", 1)
        snPrint = snPrint[0]
        snOutput = input(conf.colored(f"Enter the output folder - [default: reports/Nmap/{snPrint}/]: ","green", attrs=['bold']))
        conf.notValid(netScanFunc,snScan)
        snOutput = conf.dirOutput(snOutput, "reports/Nmap/", snPrint)
        conf.createDir(snOutput)
            
        print("______________________________________________________________________")
        
        conf.os.system(f"sudo nmap -sn {snScan} -o {snOutput}/netscan.txt")
        
        print("______________________________________________________________________")

    def menuFunc() :
        conf.clear()
        conf.reOpen()

    print("================================================")
    print( conf.colored(conf.text2art ("Nmap Scan", "small"),'cyan'))
    print("================================================")
    print( conf.colored("\n1. Scan An IP Address For Open Ports using TCP", 'yellow', attrs=['bold']))
    print( conf.colored("2. Scan An IP Address For Open Ports using UDP", 'yellow', attrs=['bold']))
    print( conf.colored("3. Operating System Scan", 'yellow', attrs=['bold']))
    print( conf.colored("4. Agressive Scan For An IP Address", 'yellow', attrs=['bold']))
    print( conf.colored("5. Scan The Network For All Devices", 'yellow', attrs=['bold']))
    print( conf.colored("M. Main Menu\n", 'yellow', attrs=['bold']))
    print("================================================")
    

    conf.ans = input( conf.colored("\nWhat would you like to do? Enter your selection: ", 'green')).upper()

    if conf.ans == "1":
        conf.callFunc(tcpScanFunc, 0)
    elif conf.ans == "2":
        conf.callFunc(udpScanFunc, 0)
    elif conf.ans == "3":
        conf.callFunc(osScanFunc, 0)
    elif conf.ans == "4":
        conf.callFunc(aScanFunc, 0)
    elif conf.ans == "5":
        conf.callFunc(netScanFunc, 0)
    elif conf.ans == "M":
        conf.callFunc(menuFunc, 0)
    else:
        conf.notValid(nmapScan, 0)
        
        conf.ans = None