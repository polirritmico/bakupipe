#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import unittest
#from unittest.mock import Mock, patch

from src.build import Build
from src.command import subprocess_runner

#@unittest.skip
class TestBuild(unittest.TestCase):
    def setUp(self):
        self.file = "test/build_test.yaml"
        self.build = Build(self.file)


    #@unittest.skip
    def test_load_build_files(self):
        expected_system = "Name"
        expected_repo_host = "Google Drive"
        expected_repo_url = "repository.url"
        expected_repo_user = "bakumapu"
        expected_repo_pass = "codedpass"
        expected_command_1 = "echo 'build' > file1"
        expected_command_2 = "echo 'ok' > file2"
        expected_target_directory = "build/path/"

        self.assertEqual(expected_system, self.build.system)
        self.assertEqual(expected_repo_host, self.build.repository_host)
        self.assertEqual(expected_repo_url, self.build.repository_url)
        self.assertEqual(expected_repo_user, self.build.repository_user)
        self.assertEqual(expected_repo_pass, self.build.repository_pass)
        self.assertEqual(expected_command_1, self.build.instructions[0].command)
        self.assertEqual(expected_command_2, self.build.instructions[1].command)
        self.assertEqual(expected_target_directory, self.build.target_directory)


    #@unittest.skip
    def test_check_binaries_location_and_move_files_to_target_dir(self):
        self.build.run_instructions()
        self.assertFalse(self.build.check_binaries_location())
        self.build.mv_files_to_target_dir()
        self.assertTrue(self.build.check_binaries_location())

        subprocess_runner("rm -r build")


    #@unittest.skip
    def test_deploy(self):
        pass


