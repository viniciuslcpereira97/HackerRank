#!usr/bin/env python
#-*- coding: utf-8 -*-

def count_substring(string, sub_string):
    pattern_len = len(sub_string)
    counter = 0
    for x, char in enumerate(string[:-pattern_len+1]):
        if string[x:x+(len(sub_string))] == sub_string:
            counter += 1
    return counter
