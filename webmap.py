#!/usr/bin/env python3
#
# Copyright (c) 2021 Iliass Alami Qammouri
#
# This is free software, licensed under the MIT License.
# See /LICENSE for more information.
#

import conf.conf as conf


def main():
    while conf.ans:
        print(
            "==================================================================="
        )
        print(conf.colored(conf.text2art("WebMap", "larry3d"), "cyan"))
        print(
            conf.colored("[>]", "red", attrs=["bold"]) +
            conf.colored("Created by : Anteste\n", "magenta", attrs=["bold"]))
        print(
            conf.colored("[>]", "red", attrs=["bold"]) + conf.colored(
                f"Version : {conf.version}\n", "magenta", attrs=["bold"]))
        conf.ver_check()
        print(
            "==================================================================="
        )
        print(conf.colored("\n1. Nmap Scan", "yellow", attrs=["bold"]))
        print(conf.colored("2. Dirsearch Scan", "yellow", attrs=["bold"]))
        print(conf.colored("3. Nikto Scan", "yellow", attrs=["bold"]))
        print(conf.colored("A. All the Scans", "yellow", attrs=["bold"]))
        print(conf.colored("E. Exit\n", "yellow", attrs=["bold"]))
        print(
            "==================================================================="
        )

        conf.ans = input(
            conf.colored("\nWhat would you like to do? Enter your selection: ",
                         "green")).upper()

        if conf.ans == "1":
            conf.call_def(conf.nmap_scan)
        elif conf.ans == "2":
            conf.call_def(conf.dirsearch_scan)
        elif conf.ans == "3":
            conf.call_def(conf.nikto_scan)
        elif conf.ans == "A":
            conf.call_def(conf.full_scan)
        elif conf.ans == "E":
            conf.call_def(conf.exit)
        else:
            conf.not_valid(main, conf.ans, 0)


try:
    main()
except KeyboardInterrupt:
    print("\n \n Keyboard Interrupt. ")
    conf.sys.exit()
