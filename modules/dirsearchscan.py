#!/usr/bin/env python3
#
# Copyright (c) 2021 Iliass Alami Qammouri
#
# This is free software, licensed under the MIT License.
# See /LICENSE for more information.
#

import conf.conf as conf


def dirsearch_scan():
    print(
        "===================================================================")
    print(conf.colored(conf.text2art("Dirsearch Scan", "small"), "cyan"))
    print(
        "===================================================================")

    dir_host = input(conf.colored("\nEnter target: ", "green", attrs=["bold"]))
    dir_output = input(
        conf.colored(
            f"Enter the output folder - [default: reports/Dirsearch/{dir_host}/]: ",
            "green",
            attrs=["bold"],
        ))

    conf.not_valid(dirsearch_scan, dir_host)
    dir_output = conf.dir_output(dir_output, "reports/Dirsearch", dir_host)
    conf.create_dir(dir_output)

    conf.os.system(
        f"python3 {conf.home}/.local/share/dirsearch/dirsearch.py -u {dir_host} --format plain -o {dir_output}/dirsearch.txt"
    )

    print(
        "______________________________________________________________________"
    )
