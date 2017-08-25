#!usr/bin/env python
#-*- coding: utf-8 -*-

import re

def validate(s):
    tests = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']
    for test in tests:
        print any(eval("c." + test + "()") for c in s)

if __name__ == '__main__':
    s = raw_input()
    validate(s)
