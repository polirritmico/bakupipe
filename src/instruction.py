#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html


from src.command import subprocess_runner
from src.formats import F

class Instruction:
    def __init__(self, command: str, check=True):
        self.command = command
        self.executed = False
        self.env = None
        self.check_subprocess = check

        self.passed = False
        self.output = ""
        self.error = ""
        self.returncode = -1


    def run(self):
        self.executed = True

        try:
            proc = subprocess_runner(self.command, self.check_subprocess,
                                     env=self.env)
        except Exception as err:
            self.set_log(err, env=self.env)
            raise err
        else:
            self.set_log(proc, env=self.env)


    def set_check_subprocess(self, option: bool):
        self.check_subprocess = option


    def set_env(self, env: dict):
        if not type(env) is dict:
            raise Exception("env is not a dicctionary")
        self.env = env


    def set_log(self, proc, env=None):
        self.passed = True if proc.returncode == 0 else False

        if proc is Exception:
            self.output = proc.output
            self.error = proc.stderr
            self.returncode = proc.returncode
        else:
            self.output = proc.stdout[:-1]
            self.error = proc.stderr[:-1]
            self.returncode = proc.returncode
            self.env = env


    def _get_outputs(self) -> str:
        out = ""
        if self.output != "":
            out = "\n{}{}{}{}  - ".format(F.BOLD, F.ORANGE, F.QUOTE, F.BLUE)
            out += "{}OUT: {}{}\"{}\"{}".format(F.BLUE, F.END, F.BOLD,
                                                self.output, F.END)
        if self.error != "":
            out = "\n{}{}{}{}  - ".format(F.BOLD, F.ORANGE, F.QUOTE, F.BLUE)
            out += "{}ERR: {}{}\"{}\"{}".format(F.FAIL, F.END, F.BOLD,
                                                self.error, F.END)
        if out == "":
            return "\n"
        return out + "\n"


    def _failed_log(self) -> str:
        out = "{}{}* {}".format(F.BOLD, F.ORANGE, F.BLUE)
        out += "[{}!!{}] ".format(F.FAIL, F.BLUE)

        out += "{}\"{}\"{}".format(F.GREEN, self.command, F.END)

        out += self._get_outputs()
        return out


    def _passed_log(self) -> str:
        out = "{}{}* {}".format(F.BOLD, F.ORANGE, F.BLUE)
        out += "[{}OK{}] ".format(F.OK, F.BLUE)

        out += "{}\"{}\"{}".format(F.GREEN, self.command, F.END)

        out += self._get_outputs()
        return out


    def _not_executed_log(self) -> str:
        out = "{}{}* {}".format(F.BOLD, F.ORANGE, F.BLUE)
        out += "[  ] {}Command '{}' not executed.{}"\
                .format(F.GREEN, self.command, F.END)

        return out


    def get_log(self) -> str:
        if not self.executed:
            return self._not_executed_log()
        if not self.passed:
            return self._failed_log()
        return self._passed_log()


