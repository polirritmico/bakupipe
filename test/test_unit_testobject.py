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
    def test_import_test_data(self):
        expected_name = "Automation Test Example"
        expected_description = "Test short description"
        expected_order = 1
        expected_pre_commands = [
                "touch test_output"
                ]
        expected_instructions = [
                "echo 'a test instruction/command with options'",
                "echo 'a second instruction'",
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
        self.assertEqual(expected_order, test.order)
        self.assertEqual(expected_pre_commands, test.pre_commands)
        self.assertEqual(expected_instructions, test.instructions)
        self.assertEqual(expected_post_commands, test.post_commands)
        self.assertEqual(expected_paths, test.paths)


    #@unittest.skip
    def test_run_command(self):
        test = Test(self.test_file)
        expected = "a test command with options"

        self.assertTrue(test.run())
        self.assertEqual(expected, test.get_cmd_out())


if __name__ == "__main__":
    unittest.main()

