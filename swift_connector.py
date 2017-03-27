#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 16:32:42 2017

@author: af
"""

import sh

path = "{}".format(sh.pwd())

path = path[:-1]        # Remove linebreak
path += "/apiTools/apiTools/main.swift"

swift_program = sh.swiftc(path)
result = sh.swift(path)
print(result)