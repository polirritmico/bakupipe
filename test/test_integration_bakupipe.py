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
        self.assertEqual(expected, self.bakupipe.working_branch)

        expected = "develop"
        with patch("builtins.input", return_value=""):
            output = self.bakupipe.select_target_branch()
            self.assertEqual(expected, output)

        expected = "deploy"
        with patch("builtins.input", return_value="1"):
            output = self.bakupipe.select_target_branch()
            self.assertEqual(expected, output)


    #@unittest.skip
    def test_confirmation(self):
        with patch("builtins.input", return_value="y"):
            self.assertTrue(self.bakupipe.confirmation())

        with patch("builtins.input", return_value="n"):
            self.assertFalse(self.bakupipe.confirmation())


    #@unittest.skip
    def test_change_to_working_branch_and_return(self):
        inital_branch = self.bakupipe.repository.get_current_branch()
        test_branch = "test-branch"
        self.bakupipe.working_branch = test_branch
        expected = test_branch

        self.bakupipe.change_to_working_branch()
        output = self.bakupipe.repository.get_current_branch()
        self.assertEqual(expected, output)

        self.bakupipe.repository.goto_branch(inital_branch)
        self.bakupipe.repository.remove_branch(test_branch)

        expected = inital_branch
        output = self.bakupipe.repository.get_current_branch()
        self.assertEqual(expected, output)


    #@unittest.skip
    def test_init_test_phase(self):
        self.bakupipe.init_test_phase()


class TestRun(unittest.TestCase):
    #@unittest.skip
    def test_run(self):
        print("\n\n\n*********************************************")
        args = []
        bakupipe = Bakupipe("test/")
        with patch("builtins.input", return_value=""):
            bakupipe.run(args)


#if __name__ == "__main__":
#    unittest.main()

