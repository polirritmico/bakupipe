#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import unittest

from src.log import Log


@unittest.skip
class TestLog(unittest.TestCase):
    def setUp(self):
        self.test_log = Log("a_test_command")

    #@unittest.skip
    def test_(self):
        #color = False
        #color = True
        #print("")
        #print(test.logs[0].run_report(color))
        #print(test.logs[1].run_report(color))
        pass

