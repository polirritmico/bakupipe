#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html


## Git repository
# Project repositories URLs
BAKU_URL     = "https://github.com/polirritmico/bakumapu.git"
BAKUPIPE_URL = "https://github.com/polirritmico/bakupipe.git"
PROJECT_URLS = [ BAKU_URL, BAKUPIPE_URL ]

# WORK BRANCH
WORK_BRANCH  = "pre-deploy"

# Default branches
DEFAULT_BRANCH         = "develop"
DEFAULT_DEPLOY_BRANCH  = "deploy"
DEFAULT_RELEASE_BRANCH = "release"
DEFAULT_BRANCHES_LIST  = [DEFAULT_BRANCH, DEFAULT_DEPLOY_BRANCH,
                          DEFAULT_RELEASE_BRANCH]

# Artifacts repositories commands
DRIVE_PUSH_COMMAND = "drive push -quiet"
