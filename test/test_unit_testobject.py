#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import unittest

from src.test_object import Test


#@unittest.skip
class TestTestObject(unittest.TestCase):
    def setUp(self):
        self.test_file = "test/1_test_layout.yaml"


    #@unittest.skip
    def test_import_test_data_constructor(self):
        expected_name = "Automation Test Example"
        expected_description = "Test short description"
        expected_position = 1
        expected_pre_commands = [
                "touch test_output"
                ]
        expected_commands = [
                "echo 'a test instruction/command with options'",
                "NotValid",
                ]
        expected_post_commands = [
                "cp test_ouput test_final_output.txt"
                ]
        expected_paths = [
                "src/location/test.gd",
                "src/location/target.gd",
                ]

        test = Test(self.test_file)

        self.assertEqual(expected_name, test.name)
        self.assertEqual(expected_description, test.description)
        self.assertEqual(expected_position, test.position)
        self.assertEqual(expected_pre_commands, test.pre_commands)
        self.assertEqual(expected_commands, test.commands)
        self.assertEqual(expected_post_commands, test.post_commands)
        self.assertEqual(expected_paths, test.paths)


    #@unittest.skip
    def test_run_command_output_logs(self):
        expected_stdout_1 = "a test instruction/command with options"
        expected_stderr_1 = ""
        expected_stdout_2 = ""
        expected_stderr_2 = "/bin/sh: line 1: NotValid: command not found"

        test = Test(self.test_file)
        self.assertTrue(test.run_commands(check=False))

        self.assertEqual(expected_stdout_1, test.logs[0].output)
        self.assertEqual(expected_stderr_1, test.logs[0].error)
        self.assertEqual(expected_stdout_2, test.logs[1].output)
        self.assertEqual(expected_stderr_2, test.logs[1].error)



if __name__ == "__main__":
    unittest.main()

