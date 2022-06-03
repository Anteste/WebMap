#!/usr/bin/env python3
#
# Copyright (c) 2021 Iliass Alami Qammouri
#
# This is free software, licensed under the MIT License.
# See /LICENSE for more information.
#

import conf.conf as conf


def nikto_scan():
    print("==============================================")
    print(conf.colored(conf.text2art("Nikto Scan", "small"), "cyan"))
    print("==============================================")

    nikto_host = input(
        conf.colored("\nEnter target: ", "green", attrs=["bold"]))
    nikto_output = input(
        conf.colored(
            f"Enter the output folder - [default: reports/Nikto/{nikto_host}/]: ",
            "green",
            attrs=["bold"],
        ))

    conf.not_valid(nikto_scan, nikto_host)
    nikto_output = conf.dir_output(nikto_output, "reports/Nikto", nikto_host)

    conf.create_dir(nikto_output)

    conf.os.system(f"nikto +h {nikto_host} -output {nikto_output}/nikto.txt")

    print(
        "______________________________________________________________________"
    )
