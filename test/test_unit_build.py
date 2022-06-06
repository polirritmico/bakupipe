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
        self.file = "test/build.yaml"
        #self.build = Build(self.file)


    #@unittest.skip
    def test_load_build_files(self):
        expected_system = "Name"
        expected_repo_url = "repository.url"
        expected_repo_user = "bakumapu"
        expected_repo_pass = "codedpass"
        expected_command = "build command"
        expected_target_path = "target/build/path"

        build = Build(self.file)
        self.assertEqual(expected_system, build.system)
        self.assertEqual(expected_repo_url, build.repository_url)
        self.assertEqual(expected_repo_user, build.user)
        self.assertEqual(expected_repo_pass, build.password)
        self.assertEqual(expected_command, build.instructions[0].command)
        self.assertEqual(expected_target_path, build.target_path)


