#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Estudios 6/8 (bakumapu@gmail.com)
# 
# This program is part of Bakumapu and is released under
# the GPLv2 License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import sys
from src.bakupipe import Bakupipe

if __name__ == "__main__":
    #sys.exit(bakupipe(sys.argv[1:]))
    bakupipe = Bakupipe()
    try:
        sys.exit(bakupipe.run(sys.argv[1:]))
    except Exception as err:
        print(err)
        bakupipe.failed_handler()
        print("Closing BakuPipe")
        sys.exit()

