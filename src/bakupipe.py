#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

__version__ = "0.1"


import os
import re

# Load DEFAULT values and some CONFIGS
from pipeline.config import *
# Get F.COLORS and STYLES for print output
from src.formats import F

from src.repository import Repository
from src.test_object import Test
from src.command import subprocess_runner



class Bakupipe(object):
    def __init__(self, test_path: str="pipeline"):
        try:
            self.repository = Repository()
        except Exception as err:
            raise Exception("Can't build Repository")

        self.prebuild_test_collection = []
        self.postbuild_test_collection = []
        self.test_path = test_path
        self.work_branch = WORK_BRANCH
        self.target_branch = ""
        self.initial_branch = self.repository.get_current_branch()
        if self.initial_branch != DEFAULT_BRANCH:
            raise Exception("Not in '{}' branch".format(DEFAULT_BRANCH))


    def load_tests_in_test_path(self):
        test_files_list = self.get_test_files_in_path()
        if len(test_files_list) < 1:
            raise Exception("{}Missing test files in '{}' folder{}"\
                            .format(F.FAIL, self.test_path, F.END))

        for file in test_files_list:
            test = Test(self.test_path + file)
            if test.stage == "pre-build":
                self.prebuild_test_collection.append(test)
            elif test.stage == "post-build":
                self.postbuild_test_collection.append(test)
            else:
                raise Warning("Bad test stage: '{}'".format(test.name))


    def get_test_files_in_path(self) -> list:
        all_files = next(os.walk(self.test_path))[2]
        pattern = re.compile("\d+_.+.yaml")
        return list(filter(pattern.match, all_files))


    def user_select_target_branch(self) -> str:
        selected_branch = DEFAULT_DEPLOY_BRANCH

        print("{}Select target branch for deployment:".format(F.INFO))
        print("{}{}Currently selected branch: {}'{}'"\
               .format(F.END, F.ITLC, F.QUOTE, selected_branch))
        branch_list = self.repository.get_branch_list()
        for branch in branch_list:
            print("{}{}{}) {}{}".format(F.END, F.BOLD,
                                      branch_list.index(branch) + 1,
                                      F.END, branch))
        selection = input("{}Select a branch number (or press enter): {}"\
                          .format(F.END, F.END))

        if selection == "":
            selection = branch_list.index(selected_branch)
        else:
            selection = int(selection) - 1

        if selection >= len(branch_list) or selection < 0:
            raise Exception("{}Not recognized input selection{}"\
                            .format(F.FAIL, F.END))

        selection = branch_list[selection]
        print("{}Selected deployment target branch: {}'{}'{}"\
               .format(F.INFO, F.QUOTE, selection, F.END))

        return selection


    def make_work_branch(self):
        for branch in self.repository.branches:
            if branch == self.work_branch:
                print("The work branch already exists")
                if self.confirmation("Type 'y' to remove it: "):
                    self.repository.remove_branch(branch)
                    print("Previous work branch removed")
                    break
                else:
                    raise Exception("Work branch already exists")
        print("Creating the work branch...")
        self.repository.make_branch(self.work_branch)
        print("{}OK{}".format(F.OK, F.END))


    def goto_work_branch(self):
        print("Changing to work branch...")
        self.repository.goto_branch(self.work_branch)
        print("In branch '{}'".format(self.repository.current_branch))


    def return_to_initial_branch(self):
        print("Returning to branch '{}'".format(self.initial_branch))
        self.repository.goto_branch(self.initial_branch)


    def remove_working_branch(self):
        print("Removing branch '{}'...".format(self.work_branch))
        current = self.repository.get_current_branch()
        if current == self.work_branch:
            print("In working branch '{}', moving to inital branch '{}'".\
                  format(current, self.initial_branch))
            self.repository.goto_branch(self.initial_branch)
        self.repository.remove_branch(self.work_branch)


    def confirmation(self, message="") -> bool:
        if message == "":
            message = "{}Type {}'Y'{} to confirm: {}".format(
                      F.ITLC, F.QUOTE, F.END + F.ITLC, F.END)
        if input(message).lower() != 'y':
            return False
        return True


    def clean(self):
        if self.repository.current_branch == self.initial_branch:
            return
        self.return_to_initial_branch()
        self.remove_working_branch()


    def _in_terminal(self):
        #TODO: Find a more general way, now just check for VIM environment
        vim = subprocess_runner("env | grep VIMRUNTIME", check_subprocess=False)
        if vim.stdout != "":
            return False
        return True


    def run_init_phase(self):
        print("{}Bakupipe{}".format(F.PROG, F.END))
        print("{}========{}".format(F.GREEN, F.END))
        self.repository.get_info()
        self.load_tests_in_test_path()

        self.target_branch = self.user_select_target_branch()
        if not self.confirmation():
            raise Exception("{}Not confirmed\nAborting...{}"\
                            .format(F.FAIL, F.END))
        print('\n' + F.SEP)
        print("{}Starting deployment pipeline...{}".format(F.INFO, F.END))


    def loaded_tests_report(self, collection: list) -> str:
        output = "{}Loaded tests:\n".format(F.HEAD) + F.SEP + "\n"
        for test in collection:
            output += "{}{}) {}{}".format(F.INFO, test.position, test.name,
                                            F.END)
            output += "\t{}{}{}\n".format(F.ITLC, test.description, F.END)
        output += F.GREEN + F.SEP + "\n" + F.END

        return output


    def run_tests(self, test_collection: list):
        print("Running tests...")
        for test in test_collecion:
            test.run_all()
        print("{}OK{}".format(F.OK, F.END))


    def run_prebuild_test_phase(self):
        print('\n' + F.SEP)
        print("Beginning Pre-test Phase\n")
        print("Loaded pre-tests:\n")
        print(self.loaded_tests_report(self.prebuild_test_collection))
        try:
            self.run_tests(self.prebuild_test_collection)
        except Exception as err:
            self.clean()
            raise Exception("{}Error in Pre-test Phase{}".format(F.FAIL, F.END))


    def run_build_phase(self):
        build_cmd_linux = ""
        build_cmd_win = ""
        build_cmd_android = ""


    def run(self, args: list):
        if not self._in_terminal():
            F.disable(F)

        self.run_init_phase()
        self.make_work_branch()
        self.goto_work_branch()

        self.run_prebuild_test_phase()

        self.run_build_phase()
        # Build selected plataforms
        # move binaries and files to target locations
        #self.deploy_build()
        # second test Phase

        # -----------------------------------------------
        # End
        self.return_to_initial_branch()
        self.remove_working_branch()


