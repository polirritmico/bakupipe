#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

from config import *
from src.command import Command

class Repository:
    def __init__(self):
        self.cmd_runner = Command()
        self.check_git_repo()
        self.url = self.get_current_repo()
        self.check_in_valid_repo(PROJECT_URLS)

        #self.current_branch = self.get_current_branch()
        #self.branch_list = self.get_branch_list()

        # Begin at default branch
        if self.get_current_branch() != DEFAULT_BRANCH:
            print("Moving to branch '{}'...".format(DEFAULT_BRANCH))
            self.goto_branch(DEFAULT_BRANCH)


    def get_current_repo(self) -> str:
        self.cmd_runner.set("git config --get remote.origin.url")
        if not self.cmd_runner.run():
            raise ChildProcessError("ERROR: Can't get remote.origin.url",
                                    self.cmd_runner)
        return self.cmd_runner.get_stdout()


    def check_in_valid_repo(self, expected_list: list[str]) -> bool:
        for valid_url in expected_list:
            if self.url == valid_url:
                return True
        return False


    def check_git_repo(self):
        self.cmd_runner.set("git status")
        if not self.cmd_runner.run():
            raise Exception("Not a GIT repository")


    def get_current_branch(self) -> str:
        self.cmd_runner.set("git rev-parse --abbrev-ref HEAD")
        if not self.cmd_runner.run():
            raise ChildProcessError("ERROR: Can't get current branch",
                                    self.cmd_runner.get_stdout(),
                                    self.cmd_runner.get_stderr())
        return self.cmd_runner.get_stdout()


    def get_branch_list(self):
        self.cmd_runner.set("git branch")
        self.cmd_runner.run()
        output_raw = self.cmd_runner.get_stdout()
        output = output_raw.split()

        branch_list = []
        for branch in output:
            if branch != '*':
                branch_list.append(branch)

        return branch_list


    def find_branch(self, branch: str) -> bool:
        for b in self.get_branch_list():
            if b == branch:
                return True

        return False


    def make_branch(self, new_branch: str) -> bool:
        if self.find_branch(new_branch):
            return True

        self.cmd_runner.set("git branch {}".format(new_branch))
        if not self.cmd_runner.run():
            print("ERROR: Can't create branch {}\n\tDebug: {}"\
                   .format(new_branch, self.cmd_runner.get_stderr()))
            return False

        self.branch_list = self.get_branch_list()
        return True


    def remove_branch(self, target: str) -> bool:
        if not self.find_branch(target):
            print("WARNING: Not found branch '{}'".format(target))
            return True

        self.cmd_runner.set("git branch -d {}".format(target))
        if not self.cmd_runner.run():
            print("ERROR: Can't remove branch '{}'\
                    \n\t{}".format(target, output))
            return False

        return True


    def goto_branch(self, branch: str) -> bool:
        if branch == self.get_current_branch():
            print("WARNING: Already on target branch\n\t'{}'".format(branch))
            return True

        self.cmd_runner.set("git checkout {}".format(branch))
        if not self.cmd_runner.run():
            print("ERROR: No se pudo cambiar a la rama {}".format(branch))
            print(self.cmd_runner.get_stderr())
            return False

        return True


    def print_info(self):
        print("Repository info:")
        print(SEP)
        print("URL:\t\t{}".format(self.url))
        print("Branch list:\t{}".format(self.get_branch_list()))
        print("Current branch:\t'{}'".format(self.get_current_branch()))
        print(SEP)


    def print_branch_list(self) -> dict:
        branch_list = self.get_branch_list()
        branches = {str(key + 1) : val for key, val in enumerate(branch_list)}

        for key, branch in branches.items():
            print("  {}) {}".format(key, branch))
        return branches


