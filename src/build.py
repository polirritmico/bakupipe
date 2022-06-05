#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html


from getpass import getpass
from passlib.hash import bcrypt


class Build():
    def __init__(self, file):
        self.file = file
        self.name = ""
        self.target_path = ""
        self.instructions = []
        self.user = ""
        self.key = ""

