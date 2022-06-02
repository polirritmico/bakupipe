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
        try:
            self.repository = Repository()
        except Exception as err:
            raise Exception("Can't build Repository")
        self.test_collection = []
        self.test_path = test_path
        self.working_branch = ""


    def load_tests(self):
        test_files = self.get_test_files_in_path()
        if len(test_files) < 1:
            raise Exception("Missing test files in '{}' folder"\
                            .format(self.test_path))

        for file in test_files:
            test = Test(self.test_path + file)
            self.test_collection.append(test)


    def get_test_files_in_path(self) -> list:
        all_files = next(os.walk(self.test_path))[2]
        pattern = re.compile("\d+_.+.yaml")
        return list(filter(pattern.match, all_files))


    def get_tests_in_collection_report(self) -> str:
        output = "Loaded tests:\n" + SEP + "\n"
        for test in self.test_collection:
            output += "{}) {}\n".format(test.position, test.name)
        output += SEP + "\n"

        return output


    def select_target_branch(self) -> str:
        selected_branch = self.working_branch
        if selected_branch == "":
            selected_branch = DEFAULT_BRANCH

        print("Select target branch for deployment:")
        print("Currently selected branch: {}".format(selected_branch))
        branch_list = self.repository.get_branch_list()
        for branch in branch_list:
            print("{}) {}".format(branch_list.index(branch) + 1, branch))
        selection = input("Select a branch number (or press enter): ")

        if selection == "":
            selection = branch_list.index(selected_branch)
        else:
            selection = int(selection) - 1

        if selection >= len(branch_list) or selection < 0:
            raise Exception("Not recognized input selection")

        selection = branch_list[selection]
        print("Selected branch: '{}'".format(selection))

        return selection


    def confirmation(self, message="") -> bool:
        if message == "":
            message = "Press 'Y' to confirm: "
        if input(message).lower() != 'y':
            return False
        return True


    def make_working_branch(self):
        self.repository.make_branch(self.working_branch)
