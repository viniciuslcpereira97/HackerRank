#!usr/bin/env python
#-*- coding: utf-8 -*-

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]