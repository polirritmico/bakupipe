#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import unittest
import src.cfg

from src.repository import Repository


#@unittest.skip
class TestRepository(unittest.TestCase):
    def setUp(self):
        self.repository = Repository()
        src.cfg.init()


    #@unittest.skip
    def test_get_current_repo(self):
        expected = src.cfg.PROJECT_URLS[1]
        out = self.repository.url
        self.assertEqual(expected, out)


    #@unittest.skip
    def test_check_in_valid_repo_true(self):
        testTrue = src.cfg.PROJECT_URLS
        self.repository.check_in_valid_repo(testTrue)

        testFalse = [ "non-existing-repo" ]
        with self.assertRaises(Exception):
            self.repository.check_in_valid_repo(testFalse)


    #@unittest.skip
    def test_get_current_branch(self):
        expected = src.cfg.DEFAULT_BRANCH
        self.assertEqual(expected, self.repository.get_current_branch())


    #@unittest.skip
    def test_get_branch_list(self):
        expected = src.cfg.BRANCH_LIST
        self.assertCountEqual(expected, self.repository.get_branch_list())


    #@unittest.skip
    def test_find_branch(self):
        not_found = "non_existing_branch"
        found     = src.cfg.DEFAULT_BRANCH

        self.assertTrue(self.repository.find_branch(found))
        self.assertFalse(self.repository.find_branch(not_found))


    #@unittest.skip
    def test_get_info(self):
        expected = ""
        output = self.repository.get_info()
        self.assertNotEqual(expected, output)



