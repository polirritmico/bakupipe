#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import unittest
import os

from pipeline.config import *
from src.repository import Repository
from src.test_object import Test
from src.formats import F


#@unittest.skip
class IntegrationTests(unittest.TestCase):
    def setUp(self):
        F.disable(F)
        self.repository = Repository()


    #@unittest.skip
    def test_make_and_remove_branch(self):
        test_branch = "test-branch"
        expected_init = DEFAULT_BRANCHES_LIST
        # copy() to avoid reference to the same list object
        expected_make = expected_init.copy()
        expected_make.append(test_branch)

        self.assertCountEqual(expected_init, self.repository.get_branch_list())

        self.repository.make_branch(test_branch)
        self.assertCountEqual(expected_make, self.repository.get_branch_list())

        self.repository.remove_branch(test_branch)
        self.assertCountEqual(expected_init, self.repository.get_branch_list())


    #@unittest.skip
    def test_goto_branch(self):
        with self.assertRaises(Warning):
            self.repository.goto_branch(DEFAULT_BRANCH)

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


    #@unittest.skip
    def test_full_test_report(self):
        expected = """# Test Report: 'Integration full test'

Stage: pre-build

A test for test_integration with valid instructions

---

## Test commands

### Pre-commands

* [OK] "echo 'Bakumapu a cool old school RPG' > _temp_test_file.txt"

### Commands

* [OK] "mv _temp_test_file.txt _moved_temp_test_file.txt"
* [OK] "cat _moved_temp_test_file.txt"
  - OUT: "Bakumapu a cool old school RPG"

### Post-commands

* [OK] "rm _moved_temp_test_file.txt"
"""

        sample_test = Test("test/2_full_test.yaml")
        env = dict(os.environ)
        env["LANG"] = "C"

        sample_test.run_pre_commands()
        sample_test.run_commands()
        sample_test.run_post_commands()

        report = sample_test.full_report()

        self.assertEqual(expected, report)



