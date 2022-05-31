#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

#import sys
import os

from pipeline.config import *
from src.repository import Repository
#from src.formats import Formats


def get_test_files() -> list:
    files = [file for file in listdir(".") if isfile(join(".", f))]


def bakupipe(argv):
    print("BakuPipe\n========\n")

    print("Checking repository status")
    try:
        repository = Repository()
    except Exception as err:
        print("ERROR:\t{}".format(err))
        return -1
    print(repository.get_info())
    print("Check OK\n")

    print("Select target branch for deployment:")
    print("Currently selected branch: {}".format(DEFAULT_BRANCH))
    branch_list = repository.get_branch_list()
    for branch in branch_list:
        print("{}) {}".format(branch_list.index(branch) + 1, branch))
    print("Select a branch (or press enter): ", end="")

    selection = input()
    if selection == "":
        selection = branch_list.index(DEFAULT_BRANCH)
    else:
        selection = int(selection) - 1

    if selection >= len(branch_list) or selection < 0:
        print("Aborting...")
        return -1
    print("Selected branch: '{}'".format(branch_list[selection]))

    print("Press 'Y' to begin the deployment process: ", end="")
    if input() != 'Y':
        print("Aborting...")
        return -1

    print(SEP)
    print("Starting deployment pipeline...")
    print("Creating working branch...")
    repository.make_branch(WORK_BRANCH)
    repository.goto_branch(WORK_BRANCH)
    print("In branch '{}'...".format(repository.get_current_branch()))

    print(SEP)
    print("Starting tests...")

    test_files = get_test_files()




    return 0


