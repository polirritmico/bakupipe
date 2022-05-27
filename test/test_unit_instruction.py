#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import unittest
import os

from src.instruction import Instruction
#from src.test_object import Test

#@unittest.skip
class TestInstruction(unittest.TestCase):
    def setUp(self):
        command = 'echo "This is a \"custom\" test"'
        self.test_instruction = Instruction(command)
        self.test_instruction.env = dict(os.environ)
        self.test_instruction.env["LANG"] = "C"


    #@unittest.skip
    def test_run(self):
        expected = "This is a custom test"
        self.test_instruction.run()

        self.assertEqual('echo "This is a "custom" test"',
                         self.test_instruction.command)
        self.assertEqual(expected, self.test_instruction.output)


    #TODO: Implementar test. test not executed output. O quizás unúnico test
    #      con todo (not executed, passsed, failed)
    #@unittest.skip
    def test_get_run_log(self):
        pass

    #TODO: FIX. Update instruction functions
    #@unittest.skip
    def test_get_run_log(self):
        expected = \
"""* [OK] "a_passed_test_command"
 > - OUT: "Passed test output"
* [!!] "a_fail_test_command"
 > - ERR: "A error message\""""
        output = self.test_instruction.get_log(formats=False)

        self.assertEqual(expected, output)


@unittest.skip
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


