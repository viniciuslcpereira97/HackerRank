#!usr/bin/env python
#-*- coding: utf-8 -*-

import re

Regex_Pattern = r"\w{3}\W\w*\W\w{3}"    # Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())