#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

from src.colors import colors


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


    def line_formater(self, passed: bool):
        _output = ""
        _output += " {}{}* {}[".format(colors.BOLD, colors.ORANGE, colors.BLUE)
        if passed:
            _output += "{}OK".format(colors.OK)
        else:
            _output += "{}!!".format(colors.FAIL)
        _output += "{}]\t{}\"{}\"{}". format(colors.BLUE, colors.GREEN,
                                             self.command, colors.END)
        return _output


    def subline_formater(self, is_error: bool, message: str):
        _output = "\n   {}{}- ".format(colors.BOLD, colors.BLUE)

        if is_error:
            _output += "{}ERR: ".format(colors.FAIL)
        else:
            _output += "OUT: ".format(colors.BLUE)
        _output += "{}{}\"{}\"{}".format(colors.END, colors.BOLD,
                                         message, colors.END)

        return _output


    def run_report(self, color=True):
        _output = ""
        if not color:
            colors.disable(colors)

        if not self.passed:
            _output += self.line_formater(False)
            _output += self.subline_formater(True, self.error)
        else:
            _output = self.line_formater(True)

        if self.output != "":
            _output += self.subline_formater(False, self.output)

        return _output

