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
        file = "test/build.yaml"
        self.build = Build(file)


    #@unittest.skip
    def test_load_build_files(self):
        expected_name = "Name"
        expected_command = "build command"
        expected_build_path = "build/system"
        expected_repo_url = "repository.url"
        expected_repo_user = "bakumapu"
        expected_repo_pass = "codedpass"
        self.assertEqual(expected_name, self.build.name)

