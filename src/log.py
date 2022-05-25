#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html


class Log:
    def __init__(self, command: str):
        self.passed = False
        self.command = command
        self.path = ""
        self.output = ""
        self.error = ""
        self.returncode = -1


    def set_log(self, proc):
        self.passed = True
        self.output = proc.stdout[:-1]
        self.error = proc.stderr[:-1]
        self.returncode = proc.returncode


    def set_fail_log(self, proc):
        self.passed = False
        self.output = proc.stdout[:-1]
        self.error = proc.stderr[:-1]
        self.returncode = proc.returncode


    def get_report(self):
        _output = ""

        if self.passed:
            _output += " * [OK]\t\"{}\"\n".format(self.command)
            _output += "   - OUT: \"{}\"".format(self.output)
        else:
            _output += " * [!!]\t\"{}\"\n".format(self.command)
            _output += "   - ERR: \"{}\"".format(self.error)
            if self.output != "":
                _output += "\n   - OUT: \"{}\"".format(self.output)

        return _output

