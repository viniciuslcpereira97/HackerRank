#!usr/bin/env python
#-*- coding: utf-8 -*-

import sys

# Get all user inputs
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

# Reverse array
arr.reverse()

# Initializes output string variable
result = ""

# Concatenates all values in output string
for value in arr:
    result += "{} ".format(value)

print result