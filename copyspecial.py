#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Diarte Jeffcoat w/help from Demo from Doug Enas (https://kenzie.zoom.us/rec/play/75Asd7uorG43HNaWuQSDUfN-W47oKP6s0Skf__cMz0iyAXYEMQf3YLAWYeUKZzWAqclLlbYqrfN7_0H7?continueMode=true&_x_zm_rtaid=uaw1QT-PT1ySj6tRwudkhA.1591904168443.911291286f1b86c8f43104650acd079a&_x_zm_rhtaid=117)"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    # Create array to store paths
    special_paths = []
    file_list = []
    # Get files from directory and open
    path_dir = os.listdir(dirname)
    # for path in path_dir:
    #     if os.path.isfile(os.path.join(dirname, path)):
    #         file_list.append(path)
    # for path in path_dir:
    #     match = re.search(r"__(\w+)__", path)
    #     if match:
    #         special_paths.append(path)
    for fname in path_dir:
        match = re.search(r"__(\w+)__", fname)
        if match:
            special_paths.append(fname)
    return special_paths


def copy_to(path_list, dest_dir):
    """Copies special files to directory"""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    else:
        print("Path already exists.")

    for path in path_list:
        shutil.copy(path, dest_dir)


def zip_to(path_list, dest_zip):
    """Zip the special files into a zip file"""
    if not os.path.exists(dest_zip):
        command = ["zip", "-j", dest_zip]
        command.extend(path_list)
        print("Command I am going to do: {}".format(' '.join(command)))
        subprocess.call(command)


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    parser.add_argument('fromdir', help='src dir to look for local files')
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    all_paths = get_special_paths(ns.fromdir)

    if ns.todir:
        copy_to(all_paths, ns.todir)

    elif ns.tozip:
        zip_to(all_paths, ns.tozip)

    else:
        for path in all_paths:
            print(''.join(path))


if __name__ == "__main__":
    main(sys.argv[1:])
