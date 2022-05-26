#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html


class colors():
    CYAN = "\033[96m"   #
    BLUE = "\033[94m"   #
    ORANGE = "\033[33m"   #
    GREEN = "\033[32m"   #
    YELLOW = "\033[93m"   #ffff00

    FAIL = "\033[91m"   #ff0000
    OK = "\033[92m"   #00ff00
    WARN = YELLOW
    HEAD = "\033[95m"   #

    BOLD = "\033[1m"    # Bold
    UNDER = "\033[4m"    # Underline
    BLINK = "\033[5m"    # Blink

    # TODO: refactor, in "colors". Strange. Maybe terminal?
    QUOTE = ORANGE + " "
    END  = "\033[0m"    # End style or color

    def disable(self):
        self.CYAN = ""
        self.BLUE = ""
        self.ORANGE = ""
        self.GREEN = ""

        self.FAIL = ""
        self.OK   = ""
        self.WARN = ""
        self.HEAD = ""

        self.BOLD = ""
        self.UNDER = ""
        self.BLINK = ""

        self.QUOTE = ">"
        self.END  = ""



#if __name__ == "__main__":
#    print("Printing with colors..."
#    print(colors.CYAN + "CYAN" + colors.END)
#    print(colors.ORNG + "ORNG" + colors.END)
#    print(colors.BLUE + "BLUE" + colors.END)
#
#    print(colors.FAIL + "FAIL" + colors.END)
#    print(colors.OKGL + "OKGL" + colors.END)
#    print(colors.OKGD + "OKGD" + colors.END)
#    print(colors.WARN + "WARN" + colors.END)
#    print(colors.HEAD + "HEAD" + colors.END)
#
#    print(colors.BOLD + "BOLD" + colors.END)
#    print(colors.UNDL + "UNDL" + colors.END)
#    print(colors.BLNK + "BLNK" + colors.END)