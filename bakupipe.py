#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import sys
import subprocess

# Expected running branch
RUN_BRANCH   = "develop"
# Project repositories URLs
PROJECT_URLS = [
                 "https://github.com/polirritmico/bakumapu.git",
                 "https://github.com/polirritmico/bakupipe.git"
               ]



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
            #TODO: Raise/Catch
            return False
        return True


    def get_stdout(self):
        return self.stdout.rstrip()


    def get_stderr(self):
        return self.stderr.rstrip()


class Repository:
    def __init__(self):
        self.url = self.get_current_repo()
        #self.current_branch = self.get_current_branch()
        #self.branches = self.get_branch_list()
        self.cmd_runner = Command()

        #if not self.check_in_repo(PROJECT_URLS):
        #    raise ValueError("Repository not in project urls.", PROJECT_URLS)


    def get_current_repo() -> str:
        self.cmd_runner.set("git config --get remote.origin.url")
        if self.
        return repo_url


    #def check_in_repo(expected_list: list[str]) -> bool:
    #    for url in expected_list:
    #        if self.url == url: return True

    #    return False


    #def get_current_branch() -> str:
    #    self.cmd_runner.set("git rev-parse --abbrev-ref HEAD")
    #    if not self.cmd_runner.run():
    #        raise ValueError( "ERROR: No se puede obtener la rama actual",
    #                          self.cmd_runner.get_stdout(),
    #                          self.cmd_runner.get_stderr() )
    #    return branch


#def get_branch_list() -> list[str]:
#    branch_list = []
#    output_raw = run_command("git branch")
#    output = output_raw.split()
#
#    for branch in output:
#        if branch != '*':
#            branch_list.append(branch)
#
#    return branch_list
#
#
#def find_branch(branch: str) -> bool:
#    for b in get_branch_list():
#        if b == branch:
#            return True
#
#    return False
#
#
#def make_branch(new_branch: str) -> bool:
#    if find_branch(new_branch):
#        return False
#
#    output = run_command("git branch {}".format(new_branch))
#    #TODO: Detect and handle error
#    #if output != "":
#    #    print("ERROR: No se puede crear la rama {}\
#    #            \n\tDebug: {}".format(new_branch, output))
#    #    return False
#
#    return True
#
#
#def remove_branch(target: str) -> bool:
#    if not find_branch(target):
#        print("ADVERTENCIA: No se encuentra la rama '{}'".format(target))
#        return True
#
#    output = run_command("git branch -d {}".format(target))
#    #TODO: Detect and handle errors
#    #if output != "":
#    #    print("ERROR: No se puede borrar la rama '{}'\
#    #            \n\t{}".format(target, output))
#    #    return False
#
#    return True
#
#
#def goto_branch(branch: str) -> bool:
#    if branch == get_current_branch():
#        print("ADVERTENCIA: Actualmente en la rama de destino\
#                \n\tRama: '{}'".format(branch))
#        return True
#
#    output = run_command("git checkout {}".format(branch))
#    #TODO: Detect and handle errors
#    #if output != "":
#    #    print("ERROR: No se pudo cambiar a la rama {}".format(branch))
#    #    return False
#
#    return True
#
#
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

