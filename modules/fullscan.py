#!/usr/bin/env python3
#
# Copyright (c) 2021 Iliass Alami Qammouri
#
# This is free software, licensed under the MIT License.
# See /LICENSE for more information.
#

import conf.conf as conf

def fullScan() :
    print("===========================================================")
    print( conf.colored(conf.text2art ("All The Scans", "smAll"),'cyan'))
    print("===========================================================")

    targetAll = input( conf.colored("\nEnter the target URL : ", "green", attrs=['bold']))
    outputAll = input( conf.colored(f"Enter the output folder - [default: reports/All/{targetAll}/]: ","green", attrs=['bold']))

    conf.notValid(fullScan, targetAll)
    outputAll = conf.dirOutput(outputAll, "reports/All", targetAll)

    conf.createDir(outputAll)

    ipAll = conf.socket.gethostbyname(targetAll)

    print("___________________________________________________________________________")

    conf.createDir(outputAll)

    gnomeInstalled = True if conf.os.path.exists("/usr/bin/gnome-terminal") else False

    if len(targetAll) == 0:
        conf.clear()

        print("Not Valid Choice Try again")
        conf.reOpen()

        conf.targetAll = None
    elif gnomeInstalled:
        conf.os.system(
        'gnome-terminal -- bash -c "nmap -A '
        + ipAll
        + " -o "
        + outputAll
        + '/nmap.txt && bash"'
        )

        conf.clear()

        conf.os.system(
            'gnome-terminal -- bash -c "python3 ~/.opt/dirsearch/dirsearch.py -u '
            + targetAll
            + " --simple-report="
            + outputAll
            + '/dirsearch.txt && bash"'
        )

        conf.clear()

        conf.os.system(
            'gnome-terminal -- bash -c "nikto +h '
            + targetAll
            + " -output "
            + outputAll
            + '/nikto.txt && bash"'
        )

        conf.clear()

    else:
        conf.os.system(
        "nmap -A "
        + ipAll
        + " -o "
        + outputAll
        + "/nmap.txt"
        )

        conf.os.system(
            "python3 ~/.opt/dirsearch/dirsearch.py -u "
            + targetAll
            + " --simple-report="
            + outputAll
            + "/dirsearch.txt"
        )

        conf.os.system(
            "nikto +h "
            + targetAll
            + " -output "
            + outputAll
            + "/nikto.txt"
        )
