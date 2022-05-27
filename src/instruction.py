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

        self.passed = False
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


#    def cmd_reporter(self, command: str, fail=False) -> str:
#        _output = ""
#        _output += "{}{}* {}[".format(Formats.BOLD, colors.ORANGE, colors.BLUE)
#        if not fail:
#            _output += "{}OK".format(Formats.OK)
#        else:
#            _output += "{}!!".format(Formats.FAIL)
#        _output += "{}] {}\"{}\"{}". format(Formats.BLUE, colors.GREEN,
#                                             command, Formats.END)
#        return _output
#
#
#    def output_reporter(self, message, is_error=False) -> str:
#        _output = "\n {}{}{}{} - ".format(Formats.BOLD, colors.ORANGE,
#                                          Formats.QUOTE, colors.BLUE)
#
#        if is_error:
#            _output += "{}ERR: ".format(Formats.FAIL)
#        else:
#            _output += "OUT: ".format(Formats.BLUE)
#        _output += "{}{}\"{}\"{}".format(Formats.END, colors.BOLD,
#                                         message, Formats.END)
#
#        return _output

    def _failed_log(self) -> str:
        out = "{}{}* {}".format(Formats.BOLD, Formats.ORANGE, Formats.BLUE)
        out += "[{}!!{}] ".format(Formats.FAIL, Formats.BLUE)

        out += "{}\"{}\"{}".format(Formats.GREEN, command, Formats.END)

        return out


    def _passed_log(self) -> str:
        out = "{}{}* {}".format(Formats.BOLD, Formats.ORANGE, Formats.BLUE)
        out += "[{}OK{}] ".format(Formats.OK, Formats.BLUE)

        out += "{}\"{}\"{}".format(Formats.GREEN, command, Formats.END)

        return out


    def _not_executed_log(self) -> str:
        out = "{}{}* {}".format(Formats.BOLD, Formats.ORANGE, Formats.BLUE)
        out += "[  ] {}Command '{}' not executed.{}"\
                .format(Formats.GREEN, self.command, Formats.END)

        return out


    def get_log(self, formats=True) -> str:
        if not formats:
            Formats.disable(Formats)

        if not self.executed:
            return self._not_executed_log()
        if self.passed:
            return self._passed_log()
        return self._failed_log()


