#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import unittest
import os
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
        expected_build_directory = "./"
        expected_target_directory = "target/path/"

        self.assertEqual(expected_system, self.build.system)
        self.assertEqual(expected_repo_host, self.build.repository_host)
        self.assertEqual(expected_repo_url, self.build.repository_url)
        self.assertEqual(expected_repo_user, self.build.repository_user)
        self.assertEqual(expected_repo_pass, self.build.repository_pass)
        self.assertEqual(expected_command_1, self.build.instructions[0].command)
        self.assertEqual(expected_command_2, self.build.instructions[1].command)
        self.assertEqual(expected_build_directory, self.build.build_directory)
        self.assertEqual(expected_target_directory, self.build.target_directory)


    #@unittest.skip
    def test_checked_builded_binaries(self):
        self.build.run_instructions()
        self.assertTrue(self.build.check_builded_binaries())

        subprocess_runner("rm file1 file2")

    def test_mv_files_to_target_dir(self):
        self.build.run_instructions()
        self.build.mv_files_to_target_dir()
        self.assertFalse(self.build.check_builded_binaries())
        self.assertTrue(os.path.exists("target/path/file1"))
        self.assertTrue(os.path.exists("target/path/file2"))

        subprocess_runner("rm -r target")

    def test_same_build_and_target_folders(self):
        with self.assertRaises(Exception):
            build = Build("test/buildsame_test.yaml")


    @unittest.skip
    #TODO: create controlled build test file
    def test_push_from_target_dir_to_host_repo(self):
        self.build.push_from_target_dir_to_host_repo()


