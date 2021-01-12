import os
import sys
import socket
import string
import requests

from art import *
from termcolor import colored
from modules.dirsearchscan import dirsearchScan
from modules.niktoscan import niktoScan
from modules.nmapscan import nmapScan
from modules.fullscan import fullScan
from modules.exit import exit

ans = True
version = '1.0.4'

def reOpen():
    installed = True if os.path.exists("/bin/webmap") else False

    if installed:
        os.system("sudo webmap")

    else:
        os.system("sudo python3 webmap.py")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def createDir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def notValid(func, var, num=1) :
    num = True
    if num == True :
        if len(var) <= 5 :
            clear()

            print(colored("\nNot Valid Choice Try again\n", 'red', attrs=['reverse']))
            func()
    else :
        clear()

        print(colored("\nNot Valid Choice Try again\n", 'red', attrs=['reverse']))
        func()

def dirOutput(var, path, url) :
    if len(var) == 0 :
        var = path +"/"+ url
        return var

def callFunc(func, num=1) :
    if num == True :
        clear()
        ans = True
        while ans:
            func()
    else:
        clear()
        func()

def verCheck():
    verUrl = 'https://raw.githubusercontent.com/Anteste/WebMap/master/conf/version.txt'
    try:
        verRqst = requests.get(verUrl)
        verSc = verRqst.status_code
        if verSc == 200:
            githubVer = verRqst.text
            githubVer = githubVer.strip()

            if version == githubVer:
                print(colored(f"Your WebMap version is Up-To-Date\n",'yellow', attrs=['reverse']))
            else:
                print(colored(f"Your WebMap version is Out-Dated, New Version Available: {format(githubVer)} \n",'red', attrs=['reverse']))
        else:
            print('[ Status : {} '.format(verSc) + ']' + '\n')
    except Exception as e:
        print('\n' + '[-] Exception : ' + str(e))
