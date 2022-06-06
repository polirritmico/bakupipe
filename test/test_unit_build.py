#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import unittest
#from unittest.mock import Mock, patch

from src.build import Build

#@unittest.skip
class TestBuild(unittest.TestCase):
    def setUp(self):
        self.file = "test/build_test.yaml"
        #self.build = Build(self.file)


    #@unittest.skip
    def test_load_build_files(self):
        expected_system = "Name"
        expected_repo_host = "Google Drive"
        expected_repo_url = "repository.url"
        expected_repo_user = "bakumapu"
        expected_repo_pass = "codedpass"
        expected_command_1 = "echo 'build' > file1"
        expected_command_2 = "echo 'ok' > file2"
        expected_target_directory = "build/path"

        build = Build(self.file)
        self.assertEqual(expected_system, build.system)
        self.assertEqual(expected_repo_host, build.repository_host)
        self.assertEqual(expected_repo_url, build.repository_url)
        self.assertEqual(expected_repo_user, build.repository_user)
        self.assertEqual(expected_repo_pass, build.repository_pass)
        self.assertEqual(expected_command_1, build.instructions[0].command)
        self.assertEqual(expected_command_2, build.instructions[1].command)
        self.assertEqual(expected_target_directory, build.target_directory)


