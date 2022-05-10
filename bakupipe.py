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
BAKU_URL     = "https://github.com/polirritmico/bakumapu.git"
BAKUPIPE_URL = "https://github.com/polirritmico/bakupipe.git"


def run_command(_command: str, bypass = False):
    if bypass:
        _proc = subprocess.Popen(_command.split(),
                                 stdout=subprocess.PIPE)
        return _proc.communicate()

    _proc = subprocess.Popen(_command.split(),
                             stdout=subprocess.PIPE,
                             universal_newlines=True)
    _output = _proc.communicate()

    # Format output
    _output = str(_output[0]).rstrip()
    return _output


def get_current_repo() -> str:
    repo_url = run_command("git config --get remote.origin.url")
    return repo_url


def check_in_repo(expected_list: list[str]) -> bool:
    repo = get_current_repo()

    for url in expected_list:
        if repo == url: return True

    print("ERROR: Repositorio incorrecto\n\t{}".format(repo))
    return False


def get_current_branch() -> str:
    branch = run_command("git rev-parse --abbrev-ref HEAD")
    return branch


def check_current_branch(expected_branch) -> bool:
    current_branch = get_current_branch()

    if expected_branch != current_branch:
        print("ERROR: Rama incorrecta\n\t{}".format(current_branch))
        return False
    else:
        return True


def get_branch_list() -> list[str]:
    branch_list = []
    _output_raw = run_command("git branch", True)
    # command output (b'' string) on the first element of the tuple
    _output = _output_raw[0].split()

    for branch in _output:
        str_branch = branch.decode("UTF-8")
        if str_branch != '*':
            branch_list.append(str_branch)


def goto_branch(branch: str) -> bool:
    if branch == get_current_branch():
        print("ADVERTENCIA: Actualmente en la rama de destino\
                \n\tRama: '{}'".format(branch, RUN_BRANCH))
        return True

    output = run_command("git branch {}".format(branch))
    if output != "":
        print("ERROR: No se pudo cambiar a la rama {}".format(branch))
        return False

    return True


#def mk_pre_deploy_branch():
#    output = run_command("git checkout -b pre-deploy")
#
#    if output != "Switched to a new branch 'pre-deploy'":
#        print("ERROR: No se puede crear la rama"
#        return False
#    else:
#        return True


#def remove_branch(branch: str) -> bool:
#    output = run_command("git branch -d {}".format(branch))
#
#    if output != "":
#        return False
#    else:
#        return True


#def merge_pre_deploy():
#    pass


def main(argv):
    if len(argv) > 1:
        if argv[0] != "deploy":
            print("ERROR")
            return 1

    print("BakuPipeline\n============")
    print("Running...")

    accepted_repos = [ BAKU_URL, BAKUPIPE_URL ]

    if not check_in_repo(accepted_repos): return 1

    if not check_current_branch("pre-deploy"):
        print("Change to develop branch")
        goto_branch("develop")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

