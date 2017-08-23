#!usr/bin/env python
#-*- coding: utf-8 -*-

if __name__ == '__main__':
    n = int(raw_input())
    
    string = ""
    t = range(1, n+1)
    for num in t:
        string = string+str(num)
    print string
