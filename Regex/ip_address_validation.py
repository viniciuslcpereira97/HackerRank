#!usr/bin/env python
#-*- coding: utf-8 -*-

import re

def checkIpVersion(input):
    patterns = [
        ('IPv4', re.compile(r'^([0-9][0-9]?[0-9]?\.){3}((1[0-9]?[0-9]?)|(2[0-5]?[0-5]?)|(\d{2}))$')),
        ('IPv6', re.compile(r'^([0-9a-fA-F]{0,4}\:){7}([0-9a-fA-F]{0,4})$'))
    ]

    checked_version = "Neither"

    for ipversion, pattern in patterns:
        if re.match(pattern, string):
            checked_version = ipversion

    return checked_version

n_strings = int( raw_input() )
strings = []

for x in xrange(0,n_strings):
    strings.append( raw_input() )

for string in strings:
    print checkIpVersion(string)