#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import yaml
import os
import shutil
import re

import src.cfg

from src.instruction import Instruction
from src.formats import F

class Build():
    def __init__(self, filename):
        self.system = ""
        self.repository_host = ""
        self.repository_url = ""
        self.repository_user = ""
        self.repository_pass = ""
        self.instructions = []
        self.files = []
        self.build_directory = ""
        self.target_directory = ""

        self.import_build_file_data(filename)


    def import_build_file_data(self, filename: str):
        with open(filename, "r") as stream:
            try:
                file = yaml.safe_load(stream)
            except yaml.YAMLError as err:
                raise err

        self.system = file["SYSTEM"]
        self.repository_host = file["REPOSITORY"]["HOST"]
        self.repository_url = file["REPOSITORY"]["URL"]
        self.repository_user = file["REPOSITORY"]["USER"]
        self.repository_pass = file["REPOSITORY"]["PASS"]

        self.build_directory = file["BUILD_DIRECTORY"]
        if not self.build_directory.endswith('/'):
            self.build_directory += '/'
        self.target_directory = file["TARGET_DIRECTORY"]
        if not self.target_directory.endswith('/'):
            self.target_directory += '/'
        if self.build_directory == self.target_directory:
            raise Exception("Build and target folders can't be the same")

        instructions = file["COMMANDS"]
        for command in instructions:
            instruction = Instruction(command)
            self.instructions.append(instruction)
        build_files = file["BUILD_FILES"]
        for file in build_files:
            self.files.append(file)


    def run_instructions(self):
        for instruction in self.instructions:
            instruction.run()


    def check_builded_binaries(self) -> bool:
        for binary in self.files:
            full_path = os.path.join(self.build_directory, binary)
            if not os.path.exists(full_path):
                return False
        return True


    def mv_files_to_target_dir(self):
        if not os.path.exists(self.target_directory):
            try:
                os.makedirs(self.target_directory)
            except Exception as err:
                raise Exception("Can't make target directory", err)

        for file in self.files:
            if not os.path.exists(file):
                raise Exception("File '{}' not found".format(file))
            print("{}Moving '{}' to '{}'...{}"
                  .format(F.ITLC, file, self.target_directory, F.END))
            # shutil.move need full paths to overwrite
            target_path = os.path.join(self.target_directory, file)
            file = os.path.abspath(file)
            shutil.move(file, target_path)


    def push_from_target_dir_to_host_repo(self) -> str:
        push_message = "- '{}' build: Pushing artifacts".format(self.system)
        goto_target_dir_cmd = "cd {}".format(self.target_directory)

        # Build the cmd for supported hosts
        if self.repository_host == "Google Drive":
            # Command: $ drive push -quiet -files FILE1 FILE2 ...
            host_push_cmd = src.cfg.DRIVE_PUSH_COMMAND
            for builded_file in self.files:
                # Remove path to builded_file
                builded_file = re.sub(r".*/(.*)\.(.*)", r"\1.\2", builded_file)
                host_push_cmd += " " + builded_file
            push_message += " to Google Drive..."
        else:
            raise NotImplementedError("Not implemented repository host handler")

        # In Bash "cmd1 && cmd2": cmd2 only runs if cmd1 has no error
        push_cmd = goto_target_dir_cmd + " && " + host_push_cmd
        print(push_message)
        push_instruction = Instruction(push_cmd)
        try:
            push_instruction.run()
        except Exception as e:
            raise Exception("Failed push to {}".format(self.repository_host), e)

        return push_instruction.get_log()


