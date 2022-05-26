#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import unittest

from src.log import Log

#@unittest.skip
class TestLog(unittest.TestCase):
    def setUp(self):
        self.log_ok = Log("a_passed_test_command")
        self.log_ok.passed = True
        self.log_ok.output = "Passed test output"
        self.log_ok.error = ""
        self.log_ok.returncode = 0

        self.log_fail = Log("a_fail_test_command")
        self.log_fail.passed = False
        self.log_fail.output = ""
        self.log_fail.error = "A error message"
        self.log_fail.returncode = 1


    #@unittest.skip
    def test_run_report(self):
        expected = \
""" * [OK] "a_passed_test_command"
 > - OUT: "Passed test output"
 * [!!] "a_fail_test_command"
 > - ERR: "A error message\""""
        color = False
        output = self.log_ok.run_report(color)
        output += "\n" + self.log_fail.run_report(color)

        self.assertEqual(expected, output)

