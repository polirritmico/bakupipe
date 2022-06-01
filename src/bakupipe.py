#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

#import sys
import os
import re

from pipeline.config import *
from src.repository import Repository
from src.test_object import Test
#from src.formats import Formats


class Bakupipe(object):
    def __init__(self, test_path: str="pipeline"):
        self.repository = Repository()
        self.test_collection = []

        test_files = self.get_test_files_in_path(test_path)
        if len(test_files) < 1:
            raise Exception("Missing test files in '{}' folder"\
                            .format(test_path))

        for file in test_files:
            test = Test(test_path + file)
            self.test_collection.append(test)


    def get_test_files_in_path(self, path: str) -> list:
        all_files = next(os.walk(path))[2]
        pattern = re.compile("\d+_.+.yaml")
        return list(filter(pattern.match, all_files))


    def get_tests_in_collection_report(self) -> str:
        output = "Loaded tests:\n" + SEP + "\n"
        for test in self.test_collection:
            output += "{}) {}\n".format(test.position, test.name)
        output += SEP + "\n"

        return output


