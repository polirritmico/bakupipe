#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import subprocess
import os

#TODO: cmd = "echo "Test: test""
def subprocess_runner(command: str, env=None, check_subprocess=True):
    if env is None:
        env = dict(os.environ)

    try:
        proc = subprocess.run(command, capture_output=True,
                              encoding="utf-8", env=env,
                              shell=True, check=check_subprocess)
    except subprocess.CalledProcessError as error:
        raise error
    except Exception as error:
        raise Exception("Failed to run command '{}'".format(error.cmd),
                        error.output, error.stderr)
    else:
        return proc

