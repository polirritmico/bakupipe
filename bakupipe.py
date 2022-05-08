#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import sys
import subprocess


BAKU_URL = "https://github.com/polirritmico/bakupipe.git"
BAKUPIPE_URL = "https://github.com/polirritmico/bakumapu.git"


def run_command(_command: str) -> str:
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


def check_repo():
    repo = get_current_repo()

    return True if repo == "BAKU_URL" or repo == "BAKUPIPE_URL" else False


def get_current_branch() -> str:
    branch = run_command("git rev-parse --abbrev-ref HEAD")
    return branch


def check_branch() -> bool:
    branch = get_current_branch()



def mk_pre_deploy_branch():
    _command = "git branch -b pre-deploy"


def merge_pre_deploy():
    pass


def main(argv):
    if len(argv) > 1:
        if argv[0] != "deploy":
            print("ERROR")
            return 1

    print("BakuPipeline\n============")
    print("Running...")

    if not check_repo():
        print("ERROR: Repositorio inconrrecto")
        return 1

    if not check_branch():
        print("ERROR: rama incorrecta")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
