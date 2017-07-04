#!usr/bin/env python
#-*- coding: utf-8 -*-

import re

def get_occurrences(query, string):
    pattern = re.compile( r"\b({})\b".format(query) )
    return pattern.findall(string)

def get_string():
    N_strings = int( raw_input() )
    concat_strings = ""
    for item in range(0, N_strings):
        concat_strings += raw_input() + "\n"

    return concat_strings

def get_queries():    
    N_queries = int( raw_input() )
    queries = []

    for query in range(0, N_queries):
        queries.append( raw_input() )

    return queries

string = get_string()
queries = get_queries()

# O(n)

for query in queries:
    print len( get_occurrences( query, string ) )