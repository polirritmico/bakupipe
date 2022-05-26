#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import unittest
import os
import subprocess

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
    def test_run_command_passed_environment(self):
        expected = "C" # from setUp()
        expected_changed = "es_CL.UTF-8"
        test_cmd = "echo $LANG"

        proc = subprocess_runner(test_cmd, self.env)
        self.assertEqual(0, proc.returncode)
        self.assertEqual(expected, proc.stdout[:-1])

        self.env["LANG"] = "es_CL.UTF-8"

        proc = subprocess_runner(test_cmd, self.env)
        self.assertEqual(0, proc.returncode)
        self.assertNotEqual(expected, proc.stdout[:-1])
        self.assertEqual(expected_changed, proc.stdout[:-1])


    #@unittest.skip
    def test_run_command_not_found(self):
        test_cmd = "testcommand"
        expected = "/bin/sh: line 1: {}: command not found".format(test_cmd)

        with self.assertRaises(Exception):
            proc = subprocess_runner(test_cmd, self.env, check_subprocess=True)



if __name__ == "__main__":
    unittest.main()

