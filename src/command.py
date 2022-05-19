#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import subprocess
import os
#import sys


def subprocess_runner(command: str, environment=dict(os.environ)):
    try:
        proc = subprocess.run(command, capture_output=True, shell=True,
                              encoding="utf-8", env=environment)
    except Exception as err:
        raise Exception(
                        "Failed to run commandt '{}'".format(command),
                        git_status.stdout, git_status.stderr, err)
    return proc

#def subprocess_runner(cmd):
#    return lambda cmd : subprocess.run( cmd, capture_output=True, shell=True,
#            encoding="utf-8", env=dict(os.environ) )

