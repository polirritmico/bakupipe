#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import yaml
from src.command import Command


class Test:
    def __init__(self, testfile: str):
        # Test INFO
        self.name = ""
        self.description = ""
        self.order = 0
        # Test instructions
        self.pre_commands = []
        self.instructions = []
        self.post_commands = []
        self.paths = []
        # Test runner
        self.cmd_runner = Command()

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
        self.instructions = file["TEST"]["INSTRUCTIONS"]
        self.post_commands = file["TEST"]["POST_COMMANDS"]
        self.paths = file["TEST"]["PATHS"]


    def run(self):
        self.cmd_runner.run()



# TODO: Crear carpeta config con bakupipe.conf y test_gut.py, test_layout.test
# TODO: Desacoplar bien el run de los tests para A FUTURO poder generar un
#       sistema asíncrono de tests con señales, etc. Ahora está secuencial.
# TODO: Pasar conf.py actual a src/gloval_var o similar

