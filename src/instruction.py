#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html


from src.command import subprocess_runner
from src.formats import Formats

class Instruction:
    def __init__(self, command):
        self.command = command
        self.executed = False
        self.env = None

        self.passed = ""
        self.output = ""
        self.error = ""
        self.returncode = -1


    def run(self):
        self.executed = True

        try:
            proc = subprocess_runner(self.command, check_subprocess=True,
                                     env=self.env)
        except Exception as err:
            raise err

        self.set_log(proc)


    def set_log(self, proc, env=None):
        self.passed = True if proc.returncode == 0 else False
        self.output = proc.stdout[:-1]
        self.error = proc.stderr[:-1]
        self.returncode = proc.returncode
        self.env = env


#    def cmd_reporter(self, command: str, passed=True) -> str:
#        _output = ""
#        _output += "{}{}* {}[".format(colors.BOLD, colors.ORANGE, colors.BLUE)
#        if passed:
#            _output += "{}OK".format(colors.OK)
#        else:
#            _output += "{}!!".format(colors.FAIL)
#        _output += "{}] {}\"{}\"{}". format(colors.BLUE, colors.GREEN,
#                                             command, colors.END)
#        return _output
#
#
#    def output_reporter(self, message, is_error=False) -> str:
#        _output = "\n {}{}{}{} - ".format(colors.BOLD, colors.ORANGE,
#                                          colors.QUOTE, colors.BLUE)
#
#        if is_error:
#            _output += "{}ERR: ".format(colors.FAIL)
#        else:
#            _output += "OUT: ".format(colors.BLUE)
#        _output += "{}{}\"{}\"{}".format(colors.END, colors.BOLD,
#                                         message, colors.END)
#
#        return _output
#
#
    def run_log(self, formats=True) -> str:
        _output = ""
        if not formats:
            formats.disable(Formats)

        if not self.passed:
            _output += self.cmd_reporter(passed=False)
            _output += self.output_reporter(self.error, True)
        else:
            _output += self.cmd_reporter()

        if self.output != "":
            _output += self.output_reporter(self.output, False)

        return _output


