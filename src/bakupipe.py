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
from src.formats import Formats
from src.command import subprocess_runner


class Bakupipe(object):
    def __init__(self, test_path: str="pipeline"):
        try:
            self.repository = Repository()
        except Exception as err:
            raise Exception("Can't build Repository")

        self.test_collection = []
        self.test_path = test_path
        self.initial_branch = self.repository.get_current_branch()
        if self.initial_branch != DEFAULT_BRANCH:
            raise Exception("Not in '{}' branch".format(DEFAULT_BRANCH))
        self.work_branch = WORK_BRANCH
        self.target_branch = ""


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
        selected_branch = DEFAULT_DEPLOY_BRANCH

        print("{}Select target branch for deployment:".format(Formats.INFO))
        print("{}{}Currently selected branch: {}'{}'"\
               .format(Formats.END, Formats.ITLC, Formats.QUOTE,
                       selected_branch))
        branch_list = self.repository.get_branch_list()
        for branch in branch_list:
            print("{}{}{}) {}{}".format(Formats.END, Formats.BOLD,
                                      branch_list.index(branch) + 1,
                                      Formats.END, branch))
        selection = input("{}Select a branch number (or press enter): {}"\
                          .format(Formats.END, Formats.END))

        if selection == "":
            selection = branch_list.index(selected_branch)
        else:
            selection = int(selection) - 1

        if selection >= len(branch_list) or selection < 0:
            raise Exception("{}Not recognized input selection{}"\
                            .format(Formats.FAIL, Formats.END))

        selection = branch_list[selection]
        print("{}Selected deployment target branch: {}'{}'{}"\
               .format(Formats.INFO, Formats.QUOTE, selection, Formats.END))

        return selection


    def change_to_work_branch(self):
        print("Creating the work branch...")
        self.repository.make_branch(self.work_branch)
        print("OK")
        print("Changing to work branch...")
        self.repository.goto_branch(self.work_branch)
        print("In branch '{}'".format(self.repository.current_branch))


    def return_to_initial_branch(self):
        print("Returning to branch '{}'".format(self.initial_branch))
        self.repository.goto_branch(self.initial_branch)


    def remove_working_branch(self):
        current = self.repository.get_current_branch()
        if current == self.work_branch:
            print("In working branch '{}', moving to inital branch '{}'".\
                  format(current, self.initial_branch))
            self.repository.goto_branch(self.initial_branch)
        self.respository.remove_branch(self.work_branch)


    def init_test_phase(self):
        print("Beginning Test Phase\n" + SEP)
        for test in self.test_collection:
            print("Running test: {}".format(test.name))
            print(test.description)
            try:
                test.run_all()
            except Exception as err:
                raise err
        print("{}=== ALL TESTS PASSED ==={}".format(Formats.OK, Formats.END))


    def confirmation(self, message="") -> bool:
        if message == "":
            message = "{}Type {}'Y'{} to confirm: {}".format(
                      Formats.ITLC, Formats.QUOTE, Formats.END + Formats.ITLC,
                      Formats.END)
        if input(message).lower() != 'y':
            return False
        return True


    def run(self, args: list):
        # Check if running inside NVIM
        vim = subprocess_runner("env | grep VIMRUNTIME", check_subprocess=False)
        if vim.stdout != "":
            Formats.disable(Formats)

        print("{}Bakupipe{}".format(Formats.PROG, Formats.END))
        print("{}========{}".format(Formats.GREEN, Formats.END))
        self.repository.get_info()
        self.target_branch = self.select_target_branch()

        if not self.confirmation():
            raise Exception("{}Not confirmed\nAborting...{}"\
                            .format(Formats.FAIL, Formats.END))

        print(SEP)
        print("{}Starting deployment pipeline...{}"\
               .format(Formats.INFO, Formats.END))
        self.change_to_work_branch()

        print(SEP)
        self.init_test_phase()
        #deploy
        self.return_to_initial_branch()
        self.remove_working_branch()



