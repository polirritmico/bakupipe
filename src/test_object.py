#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import yaml

from src.instruction import Instruction


class Test:
    def __init__(self, test_file: str):
        # Test INFO
        self.name = ""
        self.description = ""
        self.stage = ""
        self.position = 0

        # Test runner
        self.pre_commands = []
        self.commands = []
        self.post_commands = []

        self.import_test_file(test_file)


    def import_test_file(self, filename: str):
        with open(filename, "r") as stream:
            try:
                file = yaml.safe_load(stream)
            except yaml.YAMLError as err:
                raise err

        self.name = file["INFO"]["NAME"]
        self.description = file["INFO"]["DESCRIPTION"]
        self.stage = file["INFO"]["STAGE"]
        self.position = self.get_order_from_filename(filename)

        instructions = file["TEST"]["COMMANDS"]
        if instructions is None:
            raise Exception("Test without command: {}".format(self.filename))
        for cmd in instructions:
            instruction = Instruction(cmd)
            self.commands.append(instruction)

        instructions = file["TEST"]["PRE_COMMANDS"]
        if instructions is not None:
            for pre_cmd in instructions:
                instruction = Instruction(pre_cmd)
                self.pre_commands.append(instruction)

        instructions = file["TEST"]["POST_COMMANDS"]
        if instructions is not None:
            for post_cmd in instructions:
                instruction = Instruction(post_cmd)
                self.post_commands.append(instruction)


    def get_order_from_filename(self, filename: str) -> int:
        filename_without_path = filename.split("/")[-1]
        position = filename_without_path.split("_")[0]
        if not position.isdecimal():
            raise Exception("Wrong filename format: {}".format(filename))

        return int(position)


    def fail_run_handler(self, instruction):
        #TODO
        raise NotImplementedError(self.__class__.__name__ + ".fail_run_handler")


    def warning_run_handler(self, instruction):
        print("WARNING")
        print(instruction.get_log())
        #TODO
        raise NotImplementedError(self.__class__.__name__ +
                                  ".warning_run_handler")


    def run_commands(self, check=True, env=None, collection=None):
        if collection is None:
            collection = self.commands
        for instruction in collection:
            print("Running test instruction:\n\t'{}'".\
                  format(instruction.command))
            if env != None:
                instruction.set_env(env)
            try:
                instruction.run()
            except Exception as error:
                #self.fail_run_handler(instruction)
                raise error
            except Warning as warning: # is a warning
                print(warning)
                self.warning_run_handler(instruction)
                continue


    def run_pre_commands(self, check=True, env=None):
        self.run_commands(check=check, env=env, collection=self.pre_commands)


    def run_post_commands(self, check=True, env=None):
        self.run_commands(check=check, env=env, collection=self.post_commands)


    # TODO: Store all this as object vars
    def run_all(self, check=True, env=None):
        self.run_pre_commands(check, env)
        self.run_commands(check, env)
        self.run_post_commands(check, env)

        #TODO: dont make full report
        return self.full_report()


    def header(self):
        header = "# Test Report: '{}'\n\n".format(self.name)
        header += "Stage: {}\n\n".format(self.stage)
        header += "{}\n\n".format(self.description)
        header += "---\n\n"
        header += "## Test commands\n\n"
        return header


    def full_report(self) -> str:
        output = ""
        output += self.header()
        output += "### Pre-commands\n\n"
        for instruction in self.pre_commands:
            output += instruction.get_log()

        output += "\n### Commands\n\n"
        for instruction in self.commands:
            output += instruction.get_log()

        output += "\n### Post-commands\n\n"
        for instruction in self.post_commands:
            output += instruction.get_log()

        return output


