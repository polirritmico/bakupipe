#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import unittest

from config import *
from src.repository import Repository


#@unittest.skip
class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.repository = Repository()


    #@unittest.skip
    def test_make_and_remove_branch(self):
        test_branch = "test-branch"
        expected_init = DEFAULT_BRANCHES_LIST
        expected_make = expected_init.copy()
        expected_make.append(test_branch)

        self.assertCountEqual(expected_init, self.repository.get_branch_list())

        self.repository.make_branch(test_branch)
        self.assertCountEqual(expected_make, self.repository.get_branch_list())

        self.repository.remove_branch(test_branch)
        self.assertCountEqual(expected_init, self.repository.get_branch_list())


    #@unittest.skip
    def test_goto_branch(self):
        print("\ntest_goto_branch:\n  Expecting a warning message...")
        self.assertTrue(self.repository.goto_branch(DEFAULT_BRANCH))
        print("\tOK\n")
        current = self.repository.get_current_branch()
        self.assertEqual(DEFAULT_BRANCH, current)

        test_branch = "test-goto-branch"
        self.repository.make_branch(test_branch)
        self.repository.goto_branch(test_branch)

        current = self.repository.get_current_branch()
        self.assertEqual(test_branch, current)

        self.repository.goto_branch(DEFAULT_BRANCH)
        current = self.repository.get_current_branch()
        self.assertEqual(DEFAULT_BRANCH, current)

        self.repository.remove_branch(test_branch)
        expected_list = DEFAULT_BRANCHES_LIST
        current_list = self.repository.get_branch_list()
        self.assertCountEqual(expected_list, current_list)



if __name__ == "__main__":
    unittest.main()

