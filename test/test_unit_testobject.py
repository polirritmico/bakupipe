#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import unittest
import os
import subprocess


from src.test_object import Test


#@unittest.skip
class TestTestObject(unittest.TestCase):
    def setUp(self):
        self.test_file = "test/1_test_layout.yaml"
        self.env = dict(os.environ)
        self.env["LANG"] = "C"


    #@unittest.skip
    def test_import_test_data_constructor(self):
        expected_name = "Automation Test Example"
        expected_description = "Test short description"
        expected_stage = "pre-build"
        expected_position = 1
        expected_pre_commands = "touch test_output"
        expected_commands_1 = "echo 'a test instruction/command with options'"
        expected_commands_2 = "NotValid"
        expected_post_commands = "cp test_ouput test_final_output.txt"

        test = Test(self.test_file)

        self.assertEqual(expected_name, test.name)
        self.assertEqual(expected_description, test.description)
        self.assertEqual(expected_stage, test.stage)
        self.assertEqual(expected_position, test.position)
        self.assertEqual(expected_pre_commands, test.pre_commands[0].command)
        self.assertEqual(expected_commands_1, test.commands[0].command)
        self.assertEqual(expected_commands_2, test.commands[1].command)
        self.assertEqual(expected_post_commands, test.post_commands[0].command)


    #@unittest.skip
    def test_import_test_data_without_pre_and_post_commands(self):
        expected_name = "No pre and post test"
        expected_description = "Test without pre and post commands"
        expected_stage = "pre-build"
        expected_position = 3
        expected_pre_cmd_len = 0
        expected_command = "echo 'a one-liner test'"
        expected_post_cmd_len = 0

        test = Test("test/3_oneliner_test.yaml")

        self.assertEqual(expected_name, test.name)
        self.assertEqual(expected_description, test.description)
        self.assertEqual(expected_stage, test.stage)
        self.assertEqual(expected_position, test.position)
        self.assertEqual(expected_pre_cmd_len, len(test.pre_commands))
        self.assertEqual(expected_command, test.commands[0].command)
        self.assertEqual(expected_post_cmd_len, len(test.post_commands))


    #@unittest.skip
    def test_run_command_output_logs(self):
        expected_stdout_1 = "a test instruction/command with options"
        expected_stderr_1 = ""
        expected_stdout_2 = ""
        expected_stderr_2 = "/bin/sh: line 1: NotValid: command not found"

        test = Test(self.test_file)

        with self.assertRaises(subprocess.CalledProcessError):
            try:
                test.run_commands(check=True, env=self.env)
            except Exception as e:
                raise e

        self.assertTrue(test.commands[0].passed)
        self.assertEqual(expected_stdout_1, test.commands[0].output)
        self.assertEqual(expected_stderr_1, test.commands[0].error)

        self.assertFalse(test.commands[1].passed)
        self.assertEqual(expected_stdout_2, test.commands[1].output)
        self.assertEqual(expected_stderr_2, test.commands[1].error)



