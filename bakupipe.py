#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import sys
import subprocess

# Project repositories URLs
BAKU_URL     = "https://github.com/polirritmico/bakumapu.git"
BAKUPIPE_URL = "https://github.com/polirritmico/bakupipe.git"

PROJECT_URLS = [ BAKU_URL, BAKUPIPE_URL ]



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


class Repository:
    def __init__(self):
        self.cmd_runner = Command()
        self.url = self.get_current_repo()
        #self.current_branch = self.get_current_branch()
        self.branch_list = self.get_branch_list()

        if not self.check_in_repo(PROJECT_URLS):
            raise ChildProcessError("Repository not in project urls.",
                                    PROJECT_URLS)


    def get_current_repo(self) -> str:
        self.cmd_runner.set("git config --get remote.origin.url")
        if not self.cmd_runner.run():
            raise ChildProcessError("ERROR: Can't get remote.origin.url",
                                    self.cmd_runner)
        return self.cmd_runner.get_stdout()


    def check_in_repo(self, expected_list: list[str]) -> bool:
        for valid_url in expected_list:
            if self.url == valid_url:
                return True
        return False


    def get_current_branch(self) -> str:
        self.cmd_runner.set("git rev-parse --abbrev-ref HEAD")
        if not self.cmd_runner.run():
            raise ChildProcessError("ERROR: Can't get current branch",
                                    self.cmd_runner.get_stdout(),
                                    self.cmd_runner.get_stderr())
        return self.cmd_runner.get_stdout()


    def update_branch_list(self):
        self.cmd_runner.set("git branch")
        self.cmd_runner.run()
        output_raw = self.cmd_runner.get_stdout()
        output = output_raw.split()

        branch_list = []
        for branch in output:
            if branch != '*':
                branch_list.append(branch)

        self.branch_list = branch_list


    def get_branch_list(self) -> list[str]:
        self.update_branch_list()
        return self.branch_list


    def find_branch(self, branch: str) -> bool:
        for b in self.branch_list:
            if b == branch:
                return True

        return False


    def make_branch(self, new_branch: str) -> bool:
        if self.find_branch(new_branch):
            return True

        self.cmd_runner.set("git branch {}".format(new_branch))
        if not self.cmd_runner.run():
            print("ERROR: No se puede crear la rama {}\n\tDebug: {}"\
                   .format(new_branch, self.cmd_runner.get_stderr()))
            return False

        self.branch_list = self.get_branch_list()
        return True


    def remove_branch(self, target: str) -> bool:
        if not self.find_branch(target):
            print("ADVERTENCIA: No se encuentra la rama '{}'".format(target))
            return True

        self.cmd_runner.set("git branch -d {}".format(target))
        if not self.cmd_runner.run():
            print("ERROR: No se puede borrar la rama '{}'\
                    \n\t{}".format(target, output))
            return False

        return True


    def goto_branch(self, branch: str) -> bool:
        if branch == self.get_current_branch():
            print("ADVERTENCIA: Actualmente en la rama de destino\
                    \n\tRama: '{}'".format(branch))
            return True

        self.cmd_runner.set("git checkout {}".format(branch))
        if not self.cmd_runner.run():
            print("ERROR: No se pudo cambiar a la rama {}".format(branch))
            print(self.cmd_runner.get_stderr())
            return False

        return True


#def check_in_current_branch(expected_branch) -> bool:
#    current_branch = get_current_branch()
#
#    if expected_branch != current_branch:
#        print("ERROR: Rama incorrecta\n\t{}".format(current_branch))
#        return False
#    return True
#
#
#def main(argv):
#    #if len(argv) > 1:
#    #    if argv[0] != "deploy":
#    #        print("ERROR")
#    #        return 1
#
#    print("BakuPipeline\n============")
#    print("Running...")
#
#    accepted_repos = [ BAKU_URL, BAKUPIPE_URL ]
#
#    if not check_in_repo(accepted_repos): return 1
#
#    if not check_current_branch("pre-deploy"):
#        print("Change to develop branch")
#        goto_branch("develop")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

