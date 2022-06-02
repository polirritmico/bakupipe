#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import unittest
from unittest.mock import Mock, patch

from src.bakupipe import Bakupipe

#@unittest.skip
class TestBakupipe(unittest.TestCase):
    def setUp(self):
        self.bakupipe = Bakupipe("test/")


    #@unittest.skip
    def test_get_test_files_in_path(self):
        expected = [ "1_test_layout.yaml", "2_full_test.yaml" ]
        output = self.bakupipe.get_test_files_in_path()

        self.assertListEqual(expected, output)


    #@unittest.skip
    def test_load_tests(self):
        self.assertEqual([], self.bakupipe.test_collection)

        self.bakupipe.load_tests()
        self.assertEqual(2, len(self.bakupipe.test_collection))

        expected = "Integration full test"
        self.assertEqual(expected, self.bakupipe.test_collection[1].name)


    #@unittest.skip
    def test_get_tests_in_collection_report(self):
        not_expected = ""
        output = self.bakupipe.get_tests_in_collection_report()
        self.assertNotEqual(not_expected, output)


    #@unittest.skip
    def test_select_target_repo(self):
        expected = ""
        self.assertEqual(expected, self.bakupipe.target_branch)

        expected = "develop"
        with patch("builtins.input", return_value=""):
            output = self.bakupipe.select_target_branch()
            self.assertEqual(expected, output)

        expected = "deploy"
        with patch("builtins.input", return_value="1"):
            output = self.bakupipe.select_target_branch()
            self.assertEqual(expected, output)

        #user_input = {"Select a branch (or press enter): ": "2"}
        #fake_input = Mock(side_effect=user_input.get)
        #with patch(self.bakupipe.select_target_branch(), fake_input):
        #    output = self.bakupipe.select_target_branch()
        #    self.assertEqual(expected, output)


#if __name__ == "__main__":
#    unittest.main()

