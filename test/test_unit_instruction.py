#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import unittest
import os

from src.instruction import Instruction
from src.formats import F


#@unittest.skip
class TestInstruction(unittest.TestCase):
    def setUp(self):
        F.disable(F)
        command = 'echo "This is a \"custom\" test"'
        self.test_instruction = Instruction(command)
        self.test_instruction.env = dict(os.environ)
        self.test_instruction.env["LANG"] = "C"


    #@unittest.skip
    def test_run(self):
        expected = "This is a custom test"
        self.test_instruction.run()

        self.assertEqual('echo "This is a "custom" test"',
                         self.test_instruction.command)
        self.assertEqual(expected, self.test_instruction.output)


    #@unittest.skip
    def test_get_run_log(self):
        cmd = "echo 'TEST'"
        expected = "* [  ] Command 'echo 'TEST'' not executed." 

        instruction = Instruction(cmd)
        self.assertFalse(instruction.executed)
        output = instruction.get_log()
        self.assertEqual(expected, output)

        # cmd = "echo 'TEST'"
        expected = "* [OK] \"echo 'TEST'\"\n  - OUT: \"TEST\"\n"

        proc = instruction.run()
        self.assertTrue(instruction.executed)
        output = instruction.get_log()

        self.assertEqual(expected, output)

        cmd_fail = "NOTEXISTING"
        expected = """* [!!] "NOTEXISTING"
  - ERR: "/bin/sh: line 1: NOTEXISTING: command not found\"\n"""
        check_subprocess = False

        instruction_fail = Instruction(cmd_fail, check_subprocess)
        fail_env = dict(os.environ)
        fail_env["LANG"] = "C"
        instruction_fail.set_env(fail_env)
        instruction_fail.run()
        output = instruction_fail.get_log()

        self.assertEqual(expected, output)



if __name__ == "__main__":
    unittest.main()


