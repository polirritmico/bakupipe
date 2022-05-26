#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import yaml
#import subprocess

from src.command import subprocess_runner
from src.log import Log


class Test:
    def __init__(self, testfile: str):
        # Test INFO
        self.name = ""
        self.description = ""
        self.position = 0
        # Test runner
        self.pre_commands = []
        self.commands = []
        self.post_commands = []
        self.paths = []
        self.logs = []

        self.import_test_file(testfile)


    def import_test_file(self, filename: str):
        with open(filename, "r") as stream:
            try:
                file = yaml.safe_load(stream)
            except yaml.YAMLError as err:
                raise err

        self.name = file["INFO"]["NAME"]
        self.description = file["INFO"]["DESCRIPTION"]
        self.position = self.get_order_from_filename(filename)

        self.pre_commands = file["TEST"]["PRE_COMMANDS"]
        self.commands = file["TEST"]["COMMANDS"]
        self.post_commands = file["TEST"]["POST_COMMANDS"]
        #TODO: Implement paths behaviour
        try:
            self.paths = file["TEST"]["PATHS"]
        except:
            self.paths = None


    def get_order_from_filename(self, filename: str) -> int:
        filename_without_path = filename.split("/")[-1]
        position = filename_without_path.split("_")[0]
        if not position.isdecimal():
            raise Exception("Wrong filename format: {}".format(filename))

        return int(position)


    def run_commands(self, check=True, env=None):
        for command in self.commands:
            log = Log(command)
            try:
                proc = subprocess_runner(command, env, check_subprocess=check)
            except Exception as e:
                log.set_fail_log(e)
                self.logs.append(log)
                raise e
            else:
                log.set_log(proc)
                self.logs.append(log)

        return True


    #def get_run_logs(self):
    #    header = "TEST INFO\n=========\n\n## {}\n\n{}\n\n"\
    #             .format(self.name, self.description)
    #    body = "## Test runners\n\n### Pre-commands\n\n"
    #    bullet = " [ ] "

    #    return header


