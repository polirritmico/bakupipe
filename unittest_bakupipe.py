#!/usr/bin/env python
#  -*- coding: utf-8 -*-

# Run with -b to hide print() output
#from src.browser import Browser

import unittest
import os

from bakupipe import *

CURRENT_REPO = "https://github.com/polirritmico/bakupipe.git"

#@unittest.skip
class TestBase(unittest.TestCase):
    def test_run_command_single_line_output(self):
        expected = "Test: la prueba funciona"
        out = run_command("echo Test: la prueba funciona")

        self.assertEqual(expected, out)

    # NOT WORKING, IMPLEMENT IF NEEDED
    #def test_run_command_multi_line_output(self):
    #    expected = """first line\nsecond line"""
    #    out = run_command("echo -e 'first line\nsecond line'")

    #    self.assertEqual(expected, out)

    def test_get_current_repo(self):
        out = get_current_repo()
        expected = CURRENT_REPO

        self.assertEqual(expected, out)


    def test_check_in_repo(self):
        testTrue = [ BAKU_URL, BAKUPIPE_URL ]
        testFalse = [ "no" ]

        self.assertTrue(check_in_repo(testTrue))
        self.assertFalse(check_in_repo(testFalse))


    def test_get_current_branch(self):
        out = get_current_branch()
        expected = "develop"

        self.assertEqual(expected, out)


    def test_get_branch_list(self):
        expected = [ "develop" ]
        output = get_branch_list()

        self.assertEqual(expected, output)


    # This test only work with a single branch in the repo named "deploy"
    def test_make_branch(self):
        test_branch = "mk-branch-test"
        default_branch = "develop"
        expected_init = [ default_branch ]
        expected_after = [ default_branch, test_branch ]

        output = get_branch_list()
        self.assertEqual(expected_init, output)

        make_branch(test_branch)
        output = get_branch_list()
        self.assertEqual(expected_after, output)


    # This test only work after test_make_remove_branch
    @unittest.skip
    def test_remove_branch(self):
        pass


    def test_goto_branch_from_target_branch(self):
        current_branch = get_current_branch()

        self.assertTrue(goto_branch(current_branch))


    @unittest.skip
    def test_goto_branch_from_another_branch(self):
        # TODO: IMPLEMENTAR MK_BRANCH y RM_BRANCH
        current = get_current_branch()
        target = current + 'B'


if __name__ == "__main__":
    unittest.main()

