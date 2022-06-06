#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import yaml
import shutil

from src.instruction import Instruction

class Build():
    def __init__(self, filename):
        self.system = ""
        self.repository_host = ""
        self.repository_url = ""
        self.repository_user = ""
        self.repository_pass = ""
        self.instructions = []
        self.files = []
        self.target_directory = ""

        self.import_build_file(filename)


    def import_build_file(self, filename: str):
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
        self.target_directory = file["TARGET_DIRECTORY"]
        if not self.target_directory.endswith('/'):
            self.target_directory += '/'

        instructions = file["COMMANDS"]
        for command in instructions:
            instruction = Instruction(command)
            self.instructions.append(instruction)
        build_files = file["BUILD_FILES"]
        for file in build_files:
            self.files.append(file)


    def run(self):
        for instruction in instructions:
            instruction.run()


    def check_binaries_location(self) -> bool:
        pass


    def mv_files_to_target_dir(self):
        for file in self.files:
            shutil.move(file, self.target_directory + file)


