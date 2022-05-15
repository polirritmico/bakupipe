#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html


class Test:
    def ___init__(self):
        gut_cmd = "godot --path $PWD --no-window -s addons/gut/gut_cmdln.gd"
        #self.cmd_runner = Command(gut_cmd)


    def import_test_data(self, test_file: str):
        pass

# TODO: Crear carpeta config con bakupipe.conf y test_gut.py, test_layout.test
# TODO: Desacoplar bien el run de los tests para A FUTURO poder generar un
#       sistema asíncrono de tests con señales, etc. Ahora está secuencial.
# TODO: Pasar conf.py actual a src/gloval_var o similar

