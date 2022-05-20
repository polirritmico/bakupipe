#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html


class Log:
    def __init__(self, command: str):
        self.passed = False
        self.command = ""
        self.path = ""
        self.output = ""
        self.error = ""
        self.returncode = -1


    def set_log(self, proc):
        self.output = proc.stdout[:-1]
        self.error = proc.stderr[:-1]
        self.returncode = proc.returncode

