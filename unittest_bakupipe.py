#!/usr/bin/env python
#  -*- coding: utf-8 -*-

# Run with -b to hide print() output
#from src.browser import Browser

import unittest
import os

from bakupipe import *

CURRENT_REPO = "https://github.com/polirritmico/bakupipe.git"
DEFAULT_BRANCH = "develop"

# NOT sort test
unittest.TestLoader.sortTestMethodsUsing = None

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
        print("Expected error:")
        self.assertFalse(check_in_repo(testFalse))
        print("\tOK")


    def test_get_current_branch(self):
        out = get_current_branch()
        expected = DEFAULT_BRANCH

        self.assertEqual(expected, out)


    def test_get_branch_list(self):
        expected = [ DEFAULT_BRANCH ]
        output = get_branch_list()

        self.assertEqual(expected, output)


    def test_find_branch(self):
        not_found = "non_existing"
        found     = DEFAULT_BRANCH

        print("Expected error:")
        self.assertFalse(find_branch(not_found))
        print("\tOK")
        self.assertTrue(find_branch(found))


    # This test only work with a single branch
    def test_make_and_remove_branch(self):
        test_branch = "test-branch"
        expected_init = [ DEFAULT_BRANCH ]
        expected_make = [ DEFAULT_BRANCH, test_branch ]

        output = get_branch_list()
        self.assertEqual(expected_init, output)

        make_branch(test_branch)
        output = get_branch_list()
        self.assertEqual(expected_make, output)

        remove_branch(test_branch)
        output = get_branch_list()
        self.assertEqual(expected_init, output)


#    @unittest.skip
#    def test_goto_branch_from_target_branch(self):
#        current_branch = get_current_branch()
#
#        self.assertTrue(goto_branch(current_branch))



class IntegrationTests(unittest.TestCase):
#    #@unittest.skip
#    def test_(self):
#        pass
#
    # This test only work after test_make_remove_branch
    #@unittest.skip
    def test_goto_branch(self):
        self.assertTrue(goto_branch(DEFAULT_BRANCH))
        current = get_current_branch()
        self.assertEqual(DEFAULT_BRANCH, current)

        test_branch = "test-goto-branch"
        make_branch(test_branch)
        goto_branch(test_branch)

        current = get_current_branch()
        self.assertEqual(test_branch, current)

        goto_branch(DEFAULT_BRANCH)
        current = get_current_branch()
        self.assertEqual(DEFAULT_BRANCH, current)

        remove_branch(test_branch)
        expected_list = [ DEFAULT_BRANCH ]
        current_list = get_branch_list()
        self.assertEqual(expected_list, current_list)



if __name__ == "__main__":
    unittest.main()

