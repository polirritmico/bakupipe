#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import yaml

from src.instruction import Instruction

class Build():
    def __init__(self, filename):
        self.system = ""
        self.repository_url = ""
        self.user = ""
        self.password = ""
        self.instructions = []
        self.target_path = ""

        self.import_build_file(filename)


    def import_build_file(self, filename: str):
        with open(filename, "r") as stream:
            try:
                file = yaml.safe_load(stream)
            except yaml.YAMLError as err:
                raise err

        self.system = file["SYSTEM"]
        self.repository_url = file["REPOSITORY"]["URL"]
        self.user = file["REPOSITORY"]["USER"]
        self.password = file["REPOSITORY"]["PASS"]
        self.target_path = file["BUILD_PATH"]

        instructions = file["COMMANDS"]
        for command in instructions:
            instruction = Instruction(command)
            self.instructions.append(instruction)


    def run(self):
        for instruction in instructions:
            instruction.run()




