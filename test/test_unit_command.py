#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import unittest
import os

from src.command import subprocess_runner


#@unittest.skip
class TestCommand(unittest.TestCase):
    def setUp(self):
        self.env = dict(os.environ)
        self.env["LANG"] = "C"


    #@unittest.skip
    def test_run_command_single_line_output(self):
        expected = "Test: all working"
        test_cmd = "echo Test: all working"

        proc = subprocess_runner(test_cmd, self.env)
        self.assertEqual(0, proc.returncode)
        self.assertEqual(expected, proc.stdout[:-1])


    #@unittest.skip
    def test_run_command_multi_line_output(self):
        expected = """first line\nsecond line"""
        test_cmd = "echo -e 'first line\nsecond line'"

        proc = subprocess_runner(test_cmd)
        self.assertEqual(0, proc.returncode)
        self.assertEqual(expected, proc.stdout[:-1])


    #@unittest.skip
    def test_run_command_LANG_environment(self):
        expected = "C"
        test_cmd = "echo $LANG"

        proc = subprocess_runner(test_cmd, self.env)
        self.assertEqual(0, proc.returncode)
        self.assertEqual(expected, proc.stdout[:-1])


    #@unittest.skip
    def test_run_command_not_found(self):
        test_cmd = "testcommand"
        expected = "/bin/sh: line 1: {}: command not found".format(test_cmd)

        proc = subprocess_runner(test_cmd, self.env)
        self.assertNotEqual(0, proc.returncode)
        self.assertEqual(expected, proc.stderr[:-1])



if __name__ == "__main__":
    unittest.main()

