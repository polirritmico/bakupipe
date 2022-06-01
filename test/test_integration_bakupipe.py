#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import unittest

from src.bakupipe import Bakupipe

#@unittest.skip
class TestBakupipe(unittest.TestCase):
#    def setUp(self):
#        pass


    #@unittest.skip
    def test_init_and_load_files(self):
        self.bakupipe = Bakupipe("test/")
        output = self.bakupipe.repository.get_info()
        self.assertNotEqual("", output)

        output = self.bakupipe.get_tests_in_collection_report()
        self.assertNotEqual("", output)


