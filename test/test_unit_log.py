#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import unittest

from src.log import Log

#TODO: Implement tests
@unittest.skip
class TestLog(unittest.TestCase):
    def setUp(self):
        self.test_log = Log("a_test_command")

#    #@unittest.skip
#    def test_(self):
#        #color = False
#        #color = True
#        #print("")
#        #print(test.logs[0].run_report(color))
#        #print(test.logs[1].run_report(color))
#        pass


    #@unittest.skip
    def test_run_report(self):
        expected=\
"""
REPORT: Automation Test Example
===============================

Test short description

## Test commands

### Pre-commands

 * [ ]
 > - [ ] {self.out,}
 * [ ] {self.precommands,}

### Commands

 * [ ] {self.commands,}
 * [ ] {self.commands,}

### Post-commands

 * [x] {self.post_commands,}
 * [ ] {self.post_commands,}

"""



if __name__ == "__main__":
    unittest.main()

