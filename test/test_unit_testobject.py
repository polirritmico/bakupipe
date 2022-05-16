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
        pass


    def test_import_test_data(self):
        test_file = "test/file_test.yaml"

        expected_name = "Automation Test Example"
        expected_description = "Test short description"
        expected_order = 1
        expected_command = "test_command --arg $PWD --arg-test -s src/location"
        expected_targets = [ "src/location/test.gd", "src/location/target.gd" ]

        test = Test(test_file)

        self.assertEqual(expected_name, test.name)
        self.assertEqual(expected_description, test.description)
        self.assertEqual(expected_order, test.order)
        self.assertEqual(expected_targets, test.targets)
        self.assertEqual(expected_command, test.command)



if __name__ == "__main__":
    unittest.main()

