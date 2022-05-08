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


def run_command(_command: str):
    _proc = subprocess.Popen(_command.split(),
                             stdout=subprocess.PIPE,
                             universal_newlines=True)
    _output = str(_proc.communicate()[0])

    return _output


def check_baku_repo():
    _command = "git config --get remote.origin.url"


def mk_pre_deploy_branch():
    _command = "git branch -b pre-deploy"


def merge_pre_deploy():
    _command = "git rev-parse --abbrev-ref HEAD"


def main(argv):
    if argv[0] != "deploy":
        print("ERROR")
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
