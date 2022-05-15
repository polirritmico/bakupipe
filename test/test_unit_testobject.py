#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import unittest

from src.test_object import Test


@unittest.skip
class TestTestObject(unittest.TestCase):
    def setUp(self):
        pass


    def test_import_test_data(self):
        expected_name = "Automation Test Example"
        expected_command = "test_command --arg $PWD --arg-test -s src/location"
        expected_targets = [ "src/location/target.gd", "src/location/t.gd" ]
        #expected_description = NotNone

        import_test = Test()
        import_test.import_test_data("layout_test")

        self.assertEqual(expected_name, self.import_test.name)
        self.assertEqual(expected_command, self.import_test.command)
        #self.assertEqual(expected_target, self.import_test.target)
        self.assertEqual(expected_targets, self.import_targets)



if __name__ == "__main__":
    unittest.main()

