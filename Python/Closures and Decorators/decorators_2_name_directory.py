#!usr/bin/env python
#-*- coding: utf-8 -*-

def person_lister(f):
    def inner(people):
        people.sort(key=lambda x: int(x[2]))
        for person in people:
            print f(person)
    return inner