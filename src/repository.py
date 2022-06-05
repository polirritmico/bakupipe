#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

#import subprocess
from pipeline.config import *
from src.command import subprocess_runner
from src.formats import F
#from src.command import Command

class Repository:
    def __init__(self):
        self.url = ""
        self.current_branch = ""
        self.branches = []

        self.check_running_in_git_repo()
        self.url = self.get_current_repo()
        self.check_in_valid_repo(PROJECT_URLS)
        self.current_branch = self.get_current_branch()
        self.branches = self.get_branch_list()

        # begin at default branch
        if self.current_branch != DEFAULT_BRANCH:
            print("Moving to branch '{}'...".format(DEFAULT_BRANCH))
            self.goto_branch(DEFAULT_BRANCH)


    def check_in_valid_repo(self, expected_list: list[str]):
        for valid_url in expected_list:
            if self.url == valid_url:
                return
        raise Exception("Not in a valid repo")


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
            raise Exception("Unable to get the current branch list from git",
                            proc.stdout, proc.stderr)
        output_raw = proc.stdout
        output = output_raw.split()

        branch_list = []
        for branch in output:
            if branch != '*':
                branch_list.append(branch)

        return branch_list


    def goto_branch(self, branch: str):
        if branch == self.get_current_branch():
            raise Warning("Already on target branch '{}'".format(branch))

        proc = subprocess_runner("git checkout {}".format(branch))
        if proc.returncode != 0:
            raise Exception("Failed to switch to branch '{}'".format(branch),
                            proc.stdout, proc.sterr)
        self.current_branch = branch


    def find_branch(self, _branch: str) -> bool:
        for branch in self.branches:
            if branch == _branch:
                return True
        return False


    def make_branch(self, new_branch: str):
        if self.find_branch(new_branch): return

        proc = subprocess_runner("git branch {}".format(new_branch))
        if proc.returncode != 0:
            raise Exception("Unable to create branch '{}'".format(new_branch),
                            proc.stdout, proc.stderr)

        self.branches = self.get_branch_list()


    def remove_branch(self, target: str):
        if not self.find_branch(target):
            raise Warning("Not found branch '{}'".format(target))

        proc = subprocess_runner("git branch -d {}".format(target))
        if proc.returncode != 0:
            raise Exception("Unable to remove branch '{}'".format(target),
                            proc.stdout, proc.sterr)

        self.branches = self.get_branch_list()


    def get_info(self):
        info = "{}".format(F.INFO)
        info += "Repository info:\n"
        info += F.SEP + "\nURL:\t\t{}{}\n{}".format(F.END, self.url, F.INFO)
        info += "Current branch:\t'{}{}'\n".format(F.END,
                                                   self.get_current_branch())
        info += "{}Branch list:\t{}{}\n".format(F.GREEN, F.END, self.branches)
        info += F.SEP + "\n"

        return info


