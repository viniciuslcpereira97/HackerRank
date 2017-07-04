#!usr/bin/env python
#-*- coding: utf-8 -*-

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
arr.reverse()
result = ""

for value in arr:
    result += "{} ".format(value)

print result