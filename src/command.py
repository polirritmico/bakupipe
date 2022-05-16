#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import subprocess
import os


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
            #TODO: 
            raise Exception("Command not set.")
            return False

        if bypass_output:
            output = subprocess.Popen(self.command, shell=True, env=self.env,
                                   stdout=subprocess.PIPE)
            for c in iter(lambda: output.stdout.read(1), b""):
                sys.stdout.buffer.write(c)
        else:
            output = subprocess.run(self.command, capture_output=True,
                                    shell=True, encoding="utf-8", env=self.env)
        self.process = output
        self.returncode = output.returncode
        self.stdout = output.stdout
        self.stderr = output.stderr

        if self.returncode != 0: # if error
            return False
        return True


    def get_stdout(self):
        return self.stdout.rstrip()


    def get_stderr(self):
        return self.stderr.rstrip()



