#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import yaml


# Check dependencies
from shutil import which
DEPENDENCIES = [ "git", "drive", ]
for dependency in DEPENDENCIES:
    if not which(dependency):
        raise Exception("Missing dependency: {}".format(dependency))


def init(filepath: str="pipeline"):
    """Must be a folder containing a valid config.yaml file"""
    filename = filepath if filepath.endswith('/') else filepath + '/'
    filename += "config.yaml"

    with open(filename, "r") as stream:
        try:
            file = yaml.safe_load(stream)
        except yaml.YAMLError as err:
            raise err

    global PROJECT_URLS
    PROJECT_URLS = file["PROJECT_URLS"]

    global WORK_BRANCH
    WORK_BRANCH = file["WORK_BRANCH"]

    global DEFAULT_BRANCH
    DEFAULT_BRANCH = file["DEFAULT_BRANCH"]
    global DEFAULT_DEPLOY_BRANCH
    DEFAULT_DEPLOY_BRANCH = file["DEFAULT_DEPLOY_BRANCH"]
    #global DEFAULT_RELEASE_BRANCH
    #DEFAULT_RELEASE_BRANCH = file["DEFAULT_RELEASE_BRANCH"]
    global BRANCH_LIST
    BRANCH_LIST = file["DEFAULT_BRANCHES_LIST"]

    #global DRIVE_PUSH_COMMAND
    #DRIVE_PUSH_COMMAND = file["DRIVE_PUSH_COMMAND"]




