#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

#import subprocess
from pipeline.config import *
from src.command import subprocess_runner
#from src.command import Command

class Repository:
    def __init__(self):
        self.check_running_in_git_repo()
        self.url = self.get_current_repo()
        self.check_in_valid_repo(PROJECT_URLS)

        self.current_branch = self.get_current_branch()
        self.branch_list = self.get_branch_list()

        # Begin at default branch
        if self.get_current_branch() != DEFAULT_BRANCH:
            print("Moving to branch '{}'...".format(DEFAULT_BRANCH))
            self.goto_branch(DEFAULT_BRANCH)


    def check_in_valid_repo(self, expected_list: list[str]) -> bool:
        for valid_url in expected_list:
            if self.url == valid_url:
                return True
        return False


    def check_running_in_git_repo(self):
        proc = subprocess_runner("git status")
        if proc.returncode != 0:
            raise Exception("Not a GIT repository", proc.stdout, proc.stderr)


    def get_current_repo(self) -> str:
        proc = subprocess_runner("git config --get remote.origin.url")
        if proc.returncode != 0:
            raise Exception("Unable to get the remote origin url",
                            proc.stdout, proc.stderr)
        return proc.stdout[:-1] # Return without \n


    def get_current_branch(self) -> str:
        proc = subprocess_runner("git rev-parse --abbrev-ref HEAD")
        if proc.returncode != 0:
            raise Exception("Unable to get the current branch",
                            proc.stdout, proc.stderr)
        return proc.stdout[:-1]


    def get_branch_list(self) -> list:
        proc = subprocess_runner("git branch")
        if proc.returncode != 0:
            raise Exception("Unable to get the current branch list",
                            proc.stdout, proc.stderr)
        output_raw = proc.stdout
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


    def make_branch(self, new_branch: str):
        if self.find_branch(new_branch): return

        proc = subprocess_runner("git branch {}".format(new_branch))
        if proc.returncode != 0:
            raise Exception("Unable to create branch '{}'".format(new_branch),
                            proc.stdout, proc.stderr)

        self.branch_list = self.get_branch_list()


    def remove_branch(self, target: str):
        if not self.find_branch(target):
            raise Warning("Not found branch '{}'".format(target))

        proc = subprocess_runner("git branch -d {}".format(target))
        if proc.returncode != 0:
            raise Exception("Unable to remove branch '{}'".format(target),
                            proc.stdout, proc.sterr)

    def goto_branch(self, branch: str):
        if branch == self.get_current_branch():
            raise Warning("Already on target branch '{}'".format(branch))

        proc = subprocess_runner("git checkout {}".format(branch))
        if proc.returncode != 0:
            raise Exception("Failed to switch to branch '{}'".format(branch),
                            proc.stdout, proc.sterr)


    def get_info(self):
        info = ""
        info += "Repository info:\n"
        info += SEP + "\nURL:\t\t{}\n".format(self.url)
        info += "Branch list:\t{}\n".format(self.get_branch_list())
        info += "Current branch:\t'{}'\n".format(self.get_current_branch())
        info += SEP + "\n"

        return info


    def print_branch_list(self) -> dict:
        branch_list = self.get_branch_list()
        branches = {str(key + 1) : val for key, val in enumerate(branch_list)}

        for key, branch in branches.items():
            print("  {}) {}".format(key, branch))
        return branches

