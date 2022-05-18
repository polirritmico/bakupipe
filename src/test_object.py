#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import yaml
import subprocess
#from src.command import Command
from src.log import Log

# TODO: Quitar cmd_runner y solo lanzar el comando y retornar logs
class Test:
    def __init__(self, testfile: str):
        # Test INFO
        self.name = ""
        self.description = ""
        self.order = 0
        # Test runner
        self.pre_commands = []
        self.commands = []
        self.post_commands = []
        self.paths = []
        # Test runner
        self.cmd_runner = Command()
        self.logs = []

        self.import_test_file(testfile)


    def _get_order_from_filename(self, filename: str) -> int:
        filename_without_path = filename.split("/")[-1]
        order = filename_without_path.split("_")[0]
        if not order.isdecimal():
            raise Exception("Wrong filename format: {}".format(filename))

        return int(order)


    def import_test_file(self, filename: str):
        with open(filename, "r") as stream:
            try:
                file = yaml.safe_load(stream)
            except yaml.YAMLError as err:
                raise err

        self.name = file["INFO"]["NAME"]
        self.description = file["INFO"]["DESCRIPTION"]
        self.order = self._get_order_from_filename(filename)

        self.pre_commands = file["TEST"]["PRE_COMMANDS"]
        self.commands = file["TEST"]["COMMANDS"]
        self.post_commands = file["TEST"]["POST_COMMANDS"]
        self.paths = file["TEST"]["PATHS"]


    def run_commands(self):
        for command in self.commands:
            self.cmd_runner.set(command)
            self.cmd_runner.run() # True para bypass output
            log = (self.cmd_runner.get_stdout(), self.cmd_runner.get_stderr())
            self.logs.append(log)

        return True

    def get_run_logs(self):
        header = "TEST INFO\n=========\n\n## {}\n\n{}\n\n"\
                 .format(self.name, self.description)
        body = "## Test runners\n\n### Pre-commands\n\n"
        bullet = " [ ] "

        return header


#   ## Test commands
#   
#   ### Pre-commands
#   
#    * [x] {self.precommands,}
#    > - [ ] {self.out,}
#    * [ ] {self.precommands,}
#   
#   ### Commands
#   
#    * [ ] {self.commands,}
#    * [ ] {self.commands,}
#   
#   ### Post-commands
#   
#    * [x] {self.post_commands,}
#    * [ ] {self.post_commands,}



