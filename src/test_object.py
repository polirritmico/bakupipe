#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import yaml

class Test:
    def __init__(self, testfile: str):
        self.name = ""
        self.description = ""
        self.order = 0
        self.command = ""
        self.targets = []
        #self.output = ""

        self.import_test_file(testfile)

    def import_test_file(self, filename: str):
        with open(filename, "r") as stream:
            try:
                file = yaml.safe_load(stream)
            except yaml.YAMLError as err:
                raise err

        self.name = file["INFO"]["NAME"]
        self.description = file["INFO"]["DESCRIPTION"]
        self.order = file["INFO"]["ORDER"]

        self.command = file["TEST"]["COMMAND"]
        self.targets = file["TEST"]["TARGETS"]



# TODO: Crear carpeta config con bakupipe.conf y test_gut.py, test_layout.test
# TODO: Desacoplar bien el run de los tests para A FUTURO poder generar un
#       sistema asíncrono de tests con señales, etc. Ahora está secuencial.
# TODO: Pasar conf.py actual a src/gloval_var o similar

