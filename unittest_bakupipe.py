#!/usr/bin/env python
#  -*- coding: utf-8 -*-

#from src.browser import Browser
#self.assertIsNotNone(out)

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

    # NOT WORKING
    #def test_run_command_multi_line_output(self):
    #    expected = """first line\nsecond line"""
    #    out = run_command("echo -e 'first line\nsecond line'")

    #    self.assertEqual(expected, out)

    def test_get_current_repo(self):
        out = get_current_repo()
        expected = CURRENT_REPO

        self.assertEqual(expected, out)


    def test_get_current_branch(self):
        out = get_current_branch()
        expected = "develop"

        self.assertEqual(expected, out)


if __name__ == "__main__":
    unittest.main()

