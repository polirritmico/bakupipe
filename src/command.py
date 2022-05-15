#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import subprocess


class Command:
    def __init__(self, _command=""):
        set(_command)


    def set(self, _command: str):
        self.reset()
        self.command = _command


    def reset(self):
        self.command = ""
        self.process = None
        self.returncode = 0
        self.stdout = ""
        self.strerr = ""


    def run(self, bypass_output = False):
        output = subprocess.run(self.command, capture_output=True,
                                shell=True, encoding="utf-8")
        self.process = output
        self.returncode = output.returncode
        self.stdout = output.stdout
        self.stderr = output.stderr

        if self.returncode != 0: # if error
            #TODO: Raise/Catch?
            #raise ChildProcessError("ERROR: subprocces return error {}",
            #                        self.stderr, self.stdout)
            return False
        return True


    def get_stdout(self):
        return self.stdout.rstrip()


    def get_stderr(self):
        return self.stderr.rstrip()



