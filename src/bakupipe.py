#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

__version__ = "0.3"


import os
import re
import getopt

# Load DEFAULT values and some CONFIGS
#from pipeline.config import *
import src.cfg
src.cfg.init()

# Get F.COLORS and STYLES for print output
from src.formats import F

from src.command import subprocess_runner
from src.repository import Repository
from src.test_object import Test
from src.build import Build



class Bakupipe(object):
    def __init__(self, files_path: str="pipeline"):
        try:
            self.repository = Repository()
        except Exception as err:
            raise Exception("Can't build Repository")

        self.in_auto_mode = False
        self.prebuild_test_collection = []
        self.postbuild_test_collection = []
        self.build_instructions = []

        self.files_path = files_path
        if not files_path.endswith('/'):
            self.files_path += '/'

        self.work_branch = src.cfg.WORK_BRANCH
        self.target_branch = ""
        self.initial_branch = self.repository.get_current_branch()
        if self.initial_branch != src.cfg.DEFAULT_BRANCH:
            raise Exception("Not in '{}' branch".format(src.cfg.DEFAULT_BRANCH))


    def help(self) -> str:
        print("BakuPipe\nUsage:")
        print("  -h | --help\t\tThis message.")
        print("  -v | --version\t\tShow the current version.")
        print("  -a | --auto\t\tNo user input mode.")


    def parse_args(self, argv: list):
        try:
            opts, args = getopt.getopt(argv, "hav",
                                       ["help", "auto", "version", ])
        except getopt.GetoptError as err:
            raise err("Bad option.")

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                self.help()
                quit()
            elif opt in ("-a", "--auto"):
                self.in_auto_mode = True
            elif opt in ("-v", "--version"):
                print("{}{}BakuPipe {}v{}{}"
                      .format(F.BOLD, F.CYAN, F.INFO, __version__, F.END))
                quit()


    def load_tests_in_files_path(self):
        search = "\d+_.+.yaml"
        test_files_list = self.get_files_matching_search_in_file_path(search)
        if test_files_list is None or len(test_files_list) < 1:
            raise Exception("{}Missing test files in '{}' folder{}"\
                    .format(F.FAIL, self.files_path[:-1], F.END))

        for file in test_files_list:
            test = Test(self.files_path + file)
            if test.stage == "pre-build":
                self.prebuild_test_collection.append(test)
            elif test.stage == "post-build":
                self.postbuild_test_collection.append(test)
            else:
                raise Warning("Bad test stage: '{}'".format(test.name))


    def load_builds_in_files_path(self):
        search = "build_.+\.yaml"
        build_files_list = self.get_files_matching_search_in_file_path(search)
        if len(build_files_list) < 1:
            raise Exception("{}Missing build files in '{}' folder{}"\
                    .format(F.FAIL, self.files_path[:-1], F.END))
        for file in build_files_list:
            build = Build(self.files_path + file)
            self.build_instructions.append(build)


    def get_files_matching_search_in_file_path(self, regex_search: str) -> list:
        pattern = re.compile(regex_search)
        if not os.path.exists(self.files_path):
            raise Exception("{}Missing folder: '{}'{}"
                            .format(F.FAIL, self.files_path, F.END))
        try:
            all_files = next(os.walk(self.files_path))[2]
        except Exception as err:
            raise Exception("{}Error searching files in path: '{}'{}"
                            .format(F.FAIL, self.files_path, F.END))
        filtered_files = list(filter(pattern.match, all_files))
        if len(filtered_files) > 1:
            filtered_files.sort()
        return filtered_files


    def user_select_target_branch(self) -> str:
        selected_branch = src.cfg.DEFAULT_DEPLOY_BRANCH
        if self.in_auto_mode:
            return selected_branch

        print("{}Select target branch for deployment:".format(F.INFO))
        print("{}{}Currently selected branch: {}'{}'"\
               .format(F.END, F.ITLC, F.QUOTE, selected_branch))
        branch_list = self.repository.get_branch_list()
        for branch in branch_list:
            if branch == selected_branch:
                print("{}{}{}) {}{}".format(F.END, F.BOLD,
                                          branch_list.index(branch) + 1,
                                          F.GREEN, branch))
            else:
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

        selected_branch = branch_list[selection]
        print("{}Selected deployment target branch: {}'{}'{}"\
               .format(F.INFO, F.QUOTE, selected_branch, F.END))

        return selected_branch


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


    def clean_working_branches(self):
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
        print(self.repository.get_info())
        print("{}Load test files...{}".format(F.ITLC, F.END))
        self.load_tests_in_files_path()
        print("{}Load build files...{}".format(F.ITLC, F.END))
        self.load_builds_in_files_path()
        print("{}Done{}\n".format(F.OK, F.END))

        print("{}Pipeline pre-run report:{}".format(F.ORANGE, F.END))
        print(F.HEAD + F.SEP + F.END)
        if len(self.prebuild_test_collection) > 0:
            print("- Loaded pre-build tests:")
            print(self.loaded_test_files_report(self.prebuild_test_collection))
        print("- Loaded build instructions:")
        print(self.loaded_build_files_report())
        if len(self.postbuild_test_collection) > 0:
            print("- Loaded post-build tests:")
            print(self.loaded_test_files_report(self.postbuild_test_collection))
        print(F.HEAD + F.SEP + F.END + '\n')

        self.target_branch = self.user_select_target_branch()
        if not self.in_auto_mode and not self.confirmation():
            raise Exception("{}Not confirmed\nAborting...{}"\
                            .format(F.FAIL, F.END))
        print('\n' + F.SEP)
        print("{}Starting deployment pipeline...{}".format(F.INFO, F.END))


    def loaded_test_files_report(self, collection: list) -> str:
        output = ""
        for test in collection:
            output += "  {}{}) {}{}".format(F.INFO, test.position, test.name,
                                          F.END)
            output += "\t{}{}{}\n".format(F.ITLC, test.description, F.END)
        return output[:-1]


    def loaded_build_files_report(self) -> str:
        #output = "{}Loaded build instructions:\n".format(F.HEAD) + F.SEP + "\n"
        output = ""
        for build in self.build_instructions:
            output += "  {}System: '{}'{}\n".format(F.INFO, build.system, F.END)
            if build.repository_url is not None:
                output += "    {}Repository URL: '{}'{}".\
                           format(F.INFO, build.repository_url, F.END)
            output += "    {}Target directory: '{}'{}\n".\
                        format(F.INFO, build.target_directory, F.END)
        return output[:-1]


    def run_tests(self, test_collection: list):
        print("Running tests...")
        for test in test_collection:
            test.run_all()
        print("{}OK{}".format(F.OK, F.END))


    def run_prebuild_test_phase(self):
        if len(self.prebuild_test_collection) == 0:
            return
        print('\n' + F.SEP)
        print("{}Beginning Pre-test Phase{}\n".format(F.ORANGE, F.END))
        #print(self.loaded_test_files_report(self.prebuild_test_collection))
        try:
            self.run_tests(self.prebuild_test_collection)
        except Exception as err:
            print("{0}{1}ERROR:{2} {1}{3}{2}".format(F.FAIL, F.BOLD, F.END, err))
            raise Exception("{}Error in Pre-test Phase{}".format(F.FAIL, F.END))


    def run_postbuild_test_phase(self):
        if len(self.postbuild_test_collection) == 0:
            return
        print('\n' + F.SEP)
        print("{}Beginning Post-test Phase{}\n".format(F.ORANGE, F.END))
        try:
            self.run_tests(self.postbuild_test_collection)
        except Exception as err:
            print("{0}{1}ERROR:{2} {1}{3}{2}".format(F.FAIL, F.BOLD, F.END, err))
            raise Exception("{}Error in Post-test Phase{}".format(F.FAIL, F.END))


    def run_build_phase(self):
        print('\n' + F.SEP)
        print("{}Beginning Build Phase{}\n".format(F.ORANGE, F.END))
        print("Building...")
        for build in self.build_instructions:
            build.run_instructions()
        print("{}Build OK{}".format(F.OK, F.END))

        print("Checking builded binaries...")
        for build in self.build_instructions:
            if not build.check_binaries_location():
                raise Exception("{}Missing binary file in build folder{}".\
                                 format(F.FAIL, F.END))
        print("{}OK{}".format(F.OK, F.END))


    def run_deploy_phase(self):
        print('\n' + F.SEP)
        print("{}Beginning Deploy Phase{}\n".format(F.ORANGE, F.END))

        #TODO: Check for old binaries into TARGET_DIRECTORY
            #TODO: If binaries are found, remove them
        #TODO: Move binaries to TARGET_DIRECTORY
            #print("Moving '{}' files to target folder".format(build.system))
            #build.mv_files_to_target_dir()

        print("Pushing artifacts to hosts servers...")
        for build in self.build_instructions:
            log = build.push_from_target_dir_to_host_repo()
            print(log)
        print("{}Deployment done{}".format(F.OK, F.END))


    def run(self, argv: list):
        self.parse_args(argv)
        if not self._in_terminal():
            F.disable(F)

        try:
            self.run_init_phase()
            self.make_work_branch()
            self.goto_work_branch()

            self.run_prebuild_test_phase()
            self.run_build_phase()
            self.run_postbuild_test_phase()

            # All OK, we can deploy
            self.run_deploy_phase()
        except Exception as err:
            self.clean_working_branches()
            raise err

        print("Cleaning the pipeline...")
        self.clean_working_branches()
        print("Exit...")


