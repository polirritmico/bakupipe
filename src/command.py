#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import subprocess
import os
#import sys


def subprocess_runner(command: str, environment=dict(os.environ),
                      check_subprocess=True):
    try:
        proc = subprocess.run(command, capture_output=True,
                              encoding="utf-8", env=environment,
                              shell=True, check=check_subprocess)
    except subprocess.CalledProcessError as e:
        raise e
    except Exception as e:
        raise Exception("Failed to run command '{}'".format(e.cmd),
                        e.output, e.stderr)
    else:
        return proc

#def subprocess_runner(cmd):
#    return lambda cmd : subprocess.run( cmd, capture_output=True, shell=True,
#            encoding="utf-8", env=dict(os.environ) )

