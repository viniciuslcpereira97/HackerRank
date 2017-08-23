#!usr/bin/env python
#-*- coding: utf-8 -*-

def mount_string(string):
    mounted_string = string
    if mounted_string[0] == '0':
        mounted_string = mounted_string[1:]
    if len(mounted_string) < 12:
        mounted_string = "91{}".format(mounted_string)
    if not mounted_string[0] == '+':
        return "+{}".format(mounted_string)
    else:
        return "{}".format(mounted_string)

def format_phone(string):
    full_string = mount_string(string)
    return "{} {} {}".format(full_string[:3], full_string[3:8], full_string[8:])

def wrapper(func):
    def format(func):
        formated = map(lambda x: format_phone(x), func)
        print '\n'.join(sorted(formated))
    return format
@wrapper
def sort_phone(l):
    return '\n'.join(sorted(l))

if __name__ == '__main__':
    l = [raw_input() for _ in range(int(input()))]
    sort_phone(l)