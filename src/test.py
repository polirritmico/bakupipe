#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html


class Test:
    def ___init__(self):
        gut_cmd = "godot --path $PWD --no-window -s addons/gut/gut_cmdln.gd"
        self.cmd_runner = Command(gut_cmd)


