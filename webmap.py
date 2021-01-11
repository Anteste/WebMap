#!/usr/bin/python3

import conf.conf as conf


def main():
    while conf.ans :
        print("===================================================================")
        print( conf.colored(conf.text2art ("WebMap", "larry3d"),'cyan'))
        print( conf.colored('[>]', "red", attrs=['bold']) + conf.colored('Created by : Anteste\n', "magenta", attrs=['bold']))
        print( conf.colored('[>]', "red", attrs=['bold']) + conf.colored("Version : 1.0.3\n",'magenta', attrs=['bold']))
        print("===================================================================")
        print( conf.colored("\n1. Nmap Scan", 'yellow', attrs=['bold']))
        print( conf.colored("2. Dirsearch Scan", 'yellow', attrs=['bold']))
        print( conf.colored("3. Nikto Scan", 'yellow', attrs=['bold']))
        print( conf.colored("A. All the Scans", 'yellow', attrs=['bold']))
        print( conf.colored("E. Exit\n", 'yellow', attrs=['bold']))
        print("===================================================================")
        
        conf.ans = input( conf.colored("\nWhat would you like to do? Enter your selection: ", 'green')).upper()

        if conf.ans == "1":
            conf.callFunc(conf.nmapScan)
        elif conf.ans == "2":
            conf.callFunc(conf.dirsearchScan)
        elif conf.ans == "3":
            conf.callFunc(conf.niktoScan)
        elif conf.ans == "A":
            conf.callFunc(conf.fullScan)
        elif conf.ans == "E":
            conf.callFunc(conf.exit)
        else:
            conf.notValid(main, conf.ans, 0)

try :
    main()
except KeyboardInterrupt:
	print('\n \n Keyboard Interrupt. ')
	conf.sys.exit()