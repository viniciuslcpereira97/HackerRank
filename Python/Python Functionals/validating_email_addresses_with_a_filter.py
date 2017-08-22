#!usr/bin/env python
#-*- coding: utf-8 -*-

import re

def fun(s):
    pattern = re.compile(r'^([\w\-]+)(@[^\W\_]*)(\..{0,3})$', re.M)
    if pattern.match(s):
        return True
    else:
        return False

def filter_mail(emails):
    return filter(fun, emails)

if __name__ == '__main__':
    n = int(raw_input())
    emails = []
    for _ in range(n):
        emails.append(raw_input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print filtered_emails