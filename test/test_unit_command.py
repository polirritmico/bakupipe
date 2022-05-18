#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import unittest

#from src.command import Command


@unittest.skip
class TestCommand(unittest.TestCase):
    def setUp(self):
        self.command_runner = Command()
        self.command_runner.env["LANG"] = "C"

    #@unittest.skip
    def test_run_command_single_line_output(self):
        expected = "Test: all working"
        test_cmd = "echo Test: all working"
        self.command_runner.set(test_cmd)

        self.assertTrue(self.command_runner.run())
        self.assertEqual(expected, self.command_runner.get_stdout())


    #@unittest.skip
    def test_run_command_multi_line_output(self):
        expected = """first line\nsecond line"""
        test_cmd = "echo -e 'first line\nsecond line'"
        self.command_runner.set(test_cmd)

        self.assertTrue(self.command_runner.run())
        self.assertEqual(expected, self.command_runner.get_stdout())


    #@unittest.skip
    def test_run_command_LANG_environment(self):
        expected = "C\n"
        self.command_runner.set("echo $LANG")

        self.assertTrue(self.command_runner.run())
        self.assertEqual(expected, self.command_runner.stdout)


    #@unittest.skip
    def test_run_command_not_found(self):
        test_cmd = "testcommand"
        expected = "/bin/sh: line 1: {}: command not found".format(test_cmd)

        self.command_runner.set(test_cmd)
        self.assertFalse(self.command_runner.run())
        self.assertEqual(expected, self.command_runner.get_stderr())



if __name__ == "__main__":
    unittest.main()

