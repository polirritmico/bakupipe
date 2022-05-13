#!/usr/bin/env python
#  -*- coding: utf-8 -*-

# Run with -b to hide print() output
#from src.browser import Browser

import unittest
import os

from bakupipe import *

# In bakupipe.py:
#BAKUPIPE_URL = "https://github.com/polirritmico/bakupipe.git"
#RUN_BRANCH = "develop"


#@unittest.skip
class TestBase(unittest.TestCase):
    #@unittest.skip
    def test_run_command_single_line_output(self):
        expected = "Test: la prueba funciona"
        out = run_command("echo Test: la prueba funciona")

        self.assertEqual(expected, out)


    #@unittest.skip
    def test_run_command_multi_line_output(self):
        expected = """first line\nsecond line"""
        out = run_command("echo -e 'first line\nsecond line'")

        self.assertEqual(expected, out)


    #@unittest.skip
    def test_run_command_not_found(self):
        test_cmd = "testcommand"
        #expected = "/bin/sh: line 1: {}: command not found".format(test_cmd)
        expected = "/bin/sh: línea 1: {}: orden no encontrada".format(test_cmd)

        print("Expected run_command error:")
        output = run_command(test_cmd)
        print("\tOK.\n")
        self.assertEqual(expected, output)


    #@unittest.skip
    def test_get_current_repo(self):
        out = get_current_repo()
        expected = BAKUPIPE_URL

        self.assertEqual(expected, out)


    #@unittest.skip
    def test_check_in_repo(self):
        testTrue = [ BAKU_URL, BAKUPIPE_URL ]
        testFalse = [ "non-existing-repo" ]

        self.assertTrue(check_in_repo(testTrue))
        self.assertFalse(check_in_repo(testFalse))


    #@unittest.skip
    def test_get_current_branch(self):
        out = get_current_branch()
        expected = RUN_BRANCH

        self.assertEqual(expected, out)


    #@unittest.skip
    def test_get_branch_list(self):
        expected = [ RUN_BRANCH ]
        output = get_branch_list()

        self.assertEqual(expected, output)


    #@unittest.skip
    def test_find_branch(self):
        not_found = "non_existing_branch"
        found     = RUN_BRANCH

        self.assertFalse(find_branch(not_found))
        self.assertTrue(find_branch(found))



class IntegrationTests(unittest.TestCase):
    # This test only work in a single branch repo
    #@unittest.skip
    def test_make_and_remove_branch(self):
        test_branch = "test-branch"
        expected_init = [ RUN_BRANCH ]
        expected_make = [ RUN_BRANCH, test_branch ]

        output = get_branch_list()
        self.assertEqual(expected_init, output)

        make_branch(test_branch)
        output = get_branch_list()
        self.assertEqual(expected_make, output)

        remove_branch(test_branch)
        output = get_branch_list()
        self.assertEqual(expected_init, output)


    #@unittest.skip
    def test_goto_branch(self):
        print("\nExpected warning message:")
        self.assertTrue(goto_branch(RUN_BRANCH))
        print("\tOK.\n")
        current = get_current_branch()
        self.assertEqual(RUN_BRANCH, current)

        test_branch = "test-goto-branch"
        make_branch(test_branch)
        goto_branch(test_branch)

        current = get_current_branch()
        self.assertEqual(test_branch, current)

        goto_branch(RUN_BRANCH)
        current = get_current_branch()
        self.assertEqual(RUN_BRANCH, current)

        remove_branch(test_branch)
        expected_list = [ RUN_BRANCH ]
        current_list = get_branch_list()
        self.assertEqual(expected_list, current_list)



if __name__ == "__main__":
    unittest.main()

