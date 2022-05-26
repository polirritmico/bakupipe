#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import yaml
#import subprocess

#from src.command import subprocess_runner
from src.instruction import Instruction
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

        instructions = file["TEST"]["PRE_COMMANDS"]
        for pre_cmd in instructions:
            instruction = Instruction(pre_cmd)
            self.pre_commands.append(instruction)

        instructions = file["TEST"]["COMMANDS"]
        for cmd in instructions:
            instruction = Instruction(cmd)
            self.commands.append(instruction)

        instructions = file["TEST"]["POST_COMMANDS"]
        for post_cmd in instructions:
            instruction = Instruction(post_cmd)
            self.post_commands.append(instruction)


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


    def full_report(self, out_format: str) -> str:
        if out_format != "":
            raise NotImplementedError

        output = ""
        output += test_header(self)
        #TODO: missing handler
        for command in self.pre_commands:
            output += ""





    #def get_run_logs(self):
    #    header = "TEST INFO\n=========\n\n## {}\n\n{}\n\n"\
    #             .format(self.name, self.description)
    #    body = "## Test runners\n\n### Pre-commands\n\n"
    #    bullet = " [ ] "

    #    return header


