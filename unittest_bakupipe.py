#!/usr/bin/env python
#  -*- coding: utf-8 -*-

# Run with -b to hide print() output
#from src.browser import Browser

import unittest
import os

from bakupipe import *



#@unittest.skip
class TestCommand(unittest.TestCase):
    def setUp(self):
        self.command_runner = Command()

    #@unittest.skip
    def test_run_command_single_line_output(self):
        expected = "Test: all working"
        test_cmd = "echo Test: all working"
        self.command_runner.set(test_cmd)

        self.assertTrue(self.command_runner.run())
        self.assertEqual(expected, self.command_runner.get_stdout())


    #@unittest.skip
    def test_run_command_multi_line_output(self):
        expected = """first line\nsecond line"""
        test_cmd = "echo -e 'first line\nsecond line'"
        self.command_runner.set(test_cmd)

        self.assertTrue(self.command_runner.run())
        self.assertEqual(expected, self.command_runner.get_stdout())


    #@unittest.skip
    def test_run_command_not_found(self):
        test_cmd = "testcommand"
        #expected = "/bin/sh: line 1: {}: command not found".format(test_cmd)
        expected = "/bin/sh: línea 1: {}: orden no encontrada".format(test_cmd)
        self.command_runner.set(test_cmd)

        self.assertFalse(self.command_runner.run())
        self.assertEqual(expected, self.command_runner.get_stderr())



#@unittest.skip
class TestRepository(unittest.TestCase):
    def setUp(self):
        self.repository = Repository()


    #@unittest.skip
    def test_get_current_repo(self):
        expected = BAKUPIPE_URL
        out = self.repository.url
        self.assertEqual(expected, out)


    #@unittest.skip
    def test_check_in_valid_repo_true(self):
        testTrue = [ BAKU_URL, BAKUPIPE_URL ]
        self.assertTrue(self.repository.check_in_valid_repo(testTrue))

        testFalse = [ "non-existing-repo" ]
        self.assertFalse(self.repository.check_in_valid_repo(testFalse))


    #@unittest.skip
    def test_get_current_branch(self):
        expected = RUN_BRANCH
        self.assertEqual(expected, self.repository.get_current_branch())


    #@unittest.skip
    def test_update_branch_list(self):
        expected = [ RUN_BRANCH ]
        self.repository.update_branch_list()
        self.assertEqual(expected, self.repository.branch_list)


    #@unittest.skip
    def test_find_branch(self):
        not_found = "non_existing_branch"
        found     = RUN_BRANCH

        self.assertTrue(self.repository.find_branch(found))
        self.assertFalse(self.repository.find_branch(not_found))


#    def test_check_git_repo(self):
#        with self.assertRaises(Exception) as context:
#            self.repository.check_git_repo()
#        self.assertTrue("Not a GIT repository" in str(context.exception))



@unittest.skip
class MainTests(unittest.TestCase):
    def test_case(self):
        pass



#@unittest.skip
class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.repository = Repository()


    # This test only work in a single branch repo
    #@unittest.skip
    def test_make_and_remove_branch(self):
        test_branch = "test-branch"
        expected_init = [ RUN_BRANCH ]
        expected_make = [ RUN_BRANCH, test_branch ]

        self.assertEqual(expected_init, self.repository.get_branch_list())

        self.repository.make_branch(test_branch)
        self.assertEqual(expected_make, self.repository.get_branch_list())

        self.repository.remove_branch(test_branch)
        self.assertEqual(expected_init, self.repository.get_branch_list())


    #@unittest.skip
    def test_goto_branch(self):
        print("\nExpected warning message:")
        self.assertTrue(self.repository.goto_branch(RUN_BRANCH))
        print("\tOK\n")
        current = self.repository.get_current_branch()
        self.assertEqual(RUN_BRANCH, current)

        test_branch = "test-goto-branch"
        self.repository.make_branch(test_branch)
        self.repository.goto_branch(test_branch)

        current = self.repository.get_current_branch()
        self.assertEqual(test_branch, current)

        self.repository.goto_branch(RUN_BRANCH)
        current = self.repository.get_current_branch()
        self.assertEqual(RUN_BRANCH, current)

        self.repository.remove_branch(test_branch)
        expected_list = [ RUN_BRANCH ]
        current_list = self.repository.get_branch_list()
        self.assertEqual(expected_list, current_list)



if __name__ == "__main__":
    unittest.main()

