#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

#import sys

from config import *
from src.repository import Repository


def bakupipe(argv):
    print("BakuPipeline\n============\n")

    print("Checking repository status")
    try:
        repository = Repository()
    except Exception as err:
        print("ERROR:\t{}".format(err))
        return -1

    repository.print_info()
    print("Check OK\n")

    print("Select target branch for deployment:")
    branches = repository.print_branch_list()
    print("Target: ", end="")
    selection = input()
    if selection == '':
        for key, val in branches.items():
            if val == DEFAULT_DEPLOY_BRANCH:
                selection = key
    if not selection in branches:
        print("Aborting...")
        return -1

    print("Selected branch: '{}'".format(branches.get(selection)))
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
    print("Starting GUT testing...")


    return 0

