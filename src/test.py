#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html


class Test:
    def ___init__(self):
        gut_cmd = "godot --path $PWD --no-window -s addons/gut/gut_cmdln.gd"
        self.cmd_runner = Command(gut_cmd)

# TODO: Crear una clase Test que importe los archivos test.test en la carpeta 
# test. Cambiar carpeta de tests TDD a bakupipe_test o similar. O usar carpeta
# config/ para leer archivos .test como test y bakupipe.conf. 
# La idea es agregar un archivo de configuración donde se lean las variables
# globales como DEFAULT_BRANCH y en la misma dejar archivos de texto de test,
# pueden ser json o un texto plano. Entonces la clase que definamos aquí tiene
# que tener un método para leer el archivo y pasarle los datos correctos al
# constructor. Luego al ejecutar la fase de test se ejecutan cada uno.
# Desacoplar bien el run de los tests para A FUTURO poder generar un sistema
# asíncrono de tests con señales, etc. Ahora lo vamos a hacer lineal.
