#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import unittest
from unittest.mock import Mock, patch

from src.bakupipe import Bakupipe
from pipeline.config import DEFAULT_DEPLOY_BRANCH

#@unittest.skip
class TestBakupipe(unittest.TestCase):
    def setUp(self):
        self.bakupipe = Bakupipe("test/")


    #@unittest.skip
    def test_get_test_files_in_path(self):
        expected = [ "1_test_layout.yaml", "2_full_test.yaml" ]
        search = "\d+_.+.yaml"
        output = self.bakupipe.get_files_matching_search_in_file_path(search)

        self.assertListEqual(expected, output)


    #@unittest.skip
    def test_load_tests(self):
        self.assertEqual([], self.bakupipe.prebuild_test_collection)
        self.assertEqual([], self.bakupipe.postbuild_test_collection)

        self.bakupipe.load_tests_in_files_path()
        self.assertEqual(2, len(self.bakupipe.prebuild_test_collection))

        expected = "Integration full test"
        self.assertEqual(expected,
                         self.bakupipe.prebuild_test_collection[1].name)


    #@unittest.skip
    def test_loaded_tests_report(self):
        not_expected = ""
        collection = self.bakupipe.prebuild_test_collection
        output = self.bakupipe.loaded_test_files_report(collection)
        self.assertNotEqual("", self.bakupipe.loaded_build_files_report())


    #@unittest.skip
    def test_user_select_target_branch(self):
        expected = ""
        self.assertEqual(expected, self.bakupipe.target_branch)

        expected = DEFAULT_DEPLOY_BRANCH
        with patch("builtins.input", return_value=""):
            output = self.bakupipe.user_select_target_branch()
            self.assertEqual(expected, output)

        expected = "release"
        with patch("builtins.input", return_value="3"):
            output = self.bakupipe.user_select_target_branch()
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
        self.bakupipe.work_branch = test_branch
        expected = test_branch

        self.bakupipe.make_work_branch()
        self.bakupipe.goto_work_branch()
        output = self.bakupipe.repository.get_current_branch()
        self.assertEqual(expected, output)

        self.bakupipe.repository.goto_branch(inital_branch)
        self.bakupipe.repository.remove_branch(test_branch)

        expected = inital_branch
        output = self.bakupipe.repository.get_current_branch()
        self.assertEqual(expected, output)


    #@unittest.skip
    def test_init_test_phase(self):
        mock = Mock()
        mock.side_effect = [ "", "y" ]
        with patch("builtins.input", mock):
            self.bakupipe.run_init_phase()


@unittest.skip
class TestRun(unittest.TestCase):
    #@unittest.skip
    def test_run(self):
        print("\n\n\n*********************************************")
        args = []
        pipeline = Bakupipe("test/")
        mock = Mock()
        mock.side_effect = [ "", "y" ]
        with self.assertRaises(Exception):
            with patch("builtins.input", mock):
                pipeline.run(args)


#if __name__ == "__main__":
#    unittest.main()

