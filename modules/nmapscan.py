#!/usr/bin/env python3
#
# Copyright (c) 2021 Iliass Alami Qammouri
#
# This is free software, licensed under the MIT License.
# See /LICENSE for more information.
#

import conf.conf as conf


def nmap_scan():
    def tcp_scan():
        conf.clear()

        print(
            "______________________________________________________________________"
        )

        tcp_host = input(
            conf.colored(
                "\nEnter the IP you want to Scan the ports of: ",
                "green",
                attrs=["bold"],
            ))
        tcp_output = input(
            conf.colored(
                f"Enter the output folder - [default: reports/Nmap/{tcp_host}/]: ",
                "green",
                attrs=["bold"],
            ))
        tcp_ip = conf.socket.gethostbyname(tcp_host)

        conf.not_valid(udp_scan, tcp_host)
        tcp_output = conf.dir_output(tcp_output, "reports/Nmap/", tcp_host)
        conf.create_dir(tcp_output)

        print(
            "______________________________________________________________________"
        )

        conf.os.system(f"nmap -sS {tcp_ip} -o {tcp_output}/tcpscan.txt")

        print(
            "______________________________________________________________________"
        )

    def udp_scan():
        print(
            "______________________________________________________________________"
        )

        udp_host = input(
            conf.colored(
                "\nEnter the IP you want to Scan the ports of: ",
                "green",
                attrs=["bold"],
            ))
        udp_output = input(
            conf.colored(
                f"Enter the output folder - [default: reports/Nmap/{udp_host}/]: ",
                "green",
                attrs=["bold"],
            ))
        udp_ip = conf.socket.gethostbyname(udp_host)

        conf.not_valid(udp_scan, udp_host)
        udp_output = conf.dir_output(udp_output, "reports/Nmap/", udp_host)
        conf.create_dir(udp_output)

        print(
            "______________________________________________________________________"
        )

        conf.os.system(f"sudo nmap -sU {udp_ip} -o {udp_output}/udpscan.txt")

        print(
            "______________________________________________________________________"
        )

    def os_scan():
        print(
            "______________________________________________________________________"
        )

        os_host = input(
            conf.colored(
                "\nEnter the IP you want to find the operating system of: ",
                "green",
                attrs=["bold"],
            ))
        os_output = input(
            conf.colored(
                f"Enter the output folder - [default: reports/Nmap/{os_host}/]: ",
                "green",
                attrs=["bold"],
            ))
        os_ip = conf.socket.gethostbyname(os_host)

        conf.not_valid(os_scan, os_host)
        os_output = conf.dir_output(os_output, "reports/Nmap/", os_host)
        conf.create_dir(os_output)

        print(
            "______________________________________________________________________"
        )

        conf.os.system(f"sudo nmap -O {os_ip} -o {os_output}/osscan.txt")

        print(
            "______________________________________________________________________"
        )

    def a_scan():
        print(
            "______________________________________________________________________"
        )

        a_host = input(
            conf.colored("\nEnter the IP you want to Scan: ",
                         "green",
                         attrs=["bold"]))
        a_output = input(
            conf.colored(
                f"Enter the output folder - [default: reports/Nmap/{a_host}/]: ",
                "green",
                attrs=["bold"],
            ))
        a_ip = conf.socket.gethostbyname(a_host)

        conf.not_valid(a_scan, a_host)
        a_output = conf.dir_output(a_output, "reports/Nmap/", a_host)
        conf.create_dir(a_output)

        print(
            "______________________________________________________________________"
        )

        conf.os.system(f"sudo nmap -T4 -A {a_ip} -o {a_output}/ascan.txt")

        print(
            "______________________________________________________________________"
        )

    def net_scan():
        conf.clear()

        print(
            "______________________________________________________________________"
        )

        net_host = input(
            conf.colored(
                "\nEnter your address and range (i.e. 192.168.0.1/24) now: ",
                "green",
                attrs=["bold"],
            ))
        net_sort = net_host.split("/", 1)
        net_sort = net_sort[0]
        sn_output = input(
            conf.colored(
                f"Enter the output folder - [default: reports/Nmap/{net_sort}/]: ",
                "green",
                attrs=["bold"],
            ))
        conf.not_valid(net_scan, net_host)
        sn_output = conf.dir_output(sn_output, "reports/Nmap/", net_sort)
        conf.create_dir(sn_output)

        print(
            "______________________________________________________________________"
        )

        conf.os.system(f"sudo nmap -sn {net_host} -o {sn_output}/netscan.txt")

        print(
            "______________________________________________________________________"
        )

    def menu_scan():
        conf.clear()
        conf.re_open()

    print("================================================")
    print(conf.colored(conf.text2art("Nmap Scan", "small"), "cyan"))
    print("================================================")
    print(
        conf.colored("\n1. Scan An IP Address For Open Ports using TCP",
                     "yellow",
                     attrs=["bold"]))
    print(
        conf.colored("2. Scan An IP Address For Open Ports using UDP",
                     "yellow",
                     attrs=["bold"]))
    print(conf.colored("3. Operating System Scan", "yellow", attrs=["bold"]))
    print(
        conf.colored("4. Agressive Scan For An IP Address",
                     "yellow",
                     attrs=["bold"]))
    print(
        conf.colored("5. Scan The Network For All Devices",
                     "yellow",
                     attrs=["bold"]))
    print(conf.colored("M. Main Menu\n", "yellow", attrs=["bold"]))
    print("================================================")

    conf.ans = input(
        conf.colored("\nWhat would you like to do? Enter your selection: ",
                     "green")).upper()

    if conf.ans == "1":
        conf.call_def(tcp_scan, 0)
    elif conf.ans == "2":
        conf.call_def(udp_scan, 0)
    elif conf.ans == "3":
        conf.call_def(os_scan, 0)
    elif conf.ans == "4":
        conf.call_def(a_scan, 0)
    elif conf.ans == "5":
        conf.call_def(net_scan, 0)
    elif conf.ans == "M":
        conf.call_def(menu_scan, 0)
    else:
        conf.not_valid(nmap_scan, 0)

        conf.ans = None
