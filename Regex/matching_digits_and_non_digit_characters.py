#!usr/bin/env python
#-*- coding: utf-8 -*-

import re

Regex_Pattern = r"(\d{2}\D){2}\d{4}"    # Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())