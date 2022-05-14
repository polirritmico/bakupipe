#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import sys
import subprocess


SEP = "-----------------------------------"

## Repository
# Project repositories URLs
BAKU_URL     = "https://github.com/polirritmico/bakumapu.git"
BAKUPIPE_URL = "https://github.com/polirritmico/bakupipe.git"
PROJECT_URLS = [ BAKU_URL, BAKUPIPE_URL ]

# Default branches
DEFAULT_BRANCH = "develop"
DEFAULT_DEPLOY_BRANCH = "deploy"
DEFAULT_BRANCHES = [ DEFAULT_BRANCH, DEFAULT_DEPLOY_BRANCH, "release" ]

# WORK BRANCH
WORK_BRANCH = "pre-deploy"

class Command:
    def __init__(self, _command=""):
        set(_command)


    def set(self, _command: str):
        self.reset()
        self.command = _command


    def reset(self):
        self.command = ""
        self.process = None
        self.returncode = 0
        self.stdout = ""
        self.strerr = ""


    def run(self, bypass_output = False):
        output = subprocess.run(self.command, capture_output=True,
                                shell=True, encoding="utf-8")
        self.process = output
        self.returncode = output.returncode
        self.stdout = output.stdout
        self.stderr = output.stderr

        if self.returncode != 0: # if error
            #TODO: Raise/Catch?
            #raise ChildProcessError("ERROR: subprocces return error {}",
            #                        self.stderr, self.stdout)
            return False
        return True


    def get_stdout(self):
        return self.stdout.rstrip()


    def get_stderr(self):
        return self.stderr.rstrip()



#class Test:
#    def ___init__(self):
#        gut_cmd = "godot --path $PWD --no-window -s addons/gut/gut_cmdln.gd"
#        self.cmd_runner = Command(gut_cmd)



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


def main(argv):
    print("BakuPipeline\n============\n")

    print("Checking repository status")
    try:
        repository = Repository()
    except Exception as err:
        print("ERROR:\t{}".format(err))
        return -1

    repository.print_info()
    print("Check OK\n")

    print("Select target branch for deployment:")
    branches = repository.print_branch_list()
    print("Target: ", end="")
    selection = input()
    if selection == '':
        for key, val in branches.items():
            if val == DEFAULT_DEPLOY_BRANCH:
                selection = key
    if not selection in branches:
        print("Aborting...")
        return -1

    print("Selected branch: '{}'".format(branches.get(selection)))
    print("Press 'Y' to begin the deployment process: ", end="")
    if input() != 'Y':
        print("Aborting...")
        return -1

    print(SEP)
    print("Starting deployment pipeline...")
    print("Creating working branch...")
    repository.make_branch(WORK_BRANCH)
    repository.goto_branch(WORK_BRANCH)
    print("In branch '{}'...".format(repository.get_current_branch()))

    print(SEP)
    print("Starting GUT testing...")


    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

