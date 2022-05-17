#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import subprocess
import os
import sys


class Command:
    def __init__(self, _command=""):
        set(_command)
        self.env = dict(os.environ)


    def set(self, _command: str):
        self.reset()
        self.command = _command


    def reset(self):
        self.command = ""
        self.process = None
        self.returncode = 0
        self.stdout = ""
        self.strerr = ""


    # TODO: Desacoplar bien el run de los tests para A FUTURO poder generar un
    #       sistema asíncrono de tests con señales, etc. Ahora está secuencial.
    # TODO: Raise/Catch? raise ChildPRocessError("message", stderr, stdout)
    def run(self, bypass_output = False):
        if self.command == "":
            raise Exception("Command not set.")
            return False

        if bypass_output:
            raise Exception("Not implemented!")
        else:
            proc = subprocess.run(self.command, capture_output=True,
                                  shell=True, encoding="utf-8", env=self.env)
        self.process = proc
        self.returncode = proc.returncode
        self.stdout = proc.stdout
        self.stderr = proc.stderr

        if self.returncode != 0: # if error
            return False
        return True


    def get_stdout(self):
        return self.stdout.rstrip()


    def get_stderr(self):
        return self.stderr.rstrip()



