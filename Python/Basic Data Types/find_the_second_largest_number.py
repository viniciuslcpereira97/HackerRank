#!usr/bin/env python
#-*- coding: utf-8 -*-

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    filtered_arr = []
    map(lambda x: filtered_arr.append(x) if x not in filtered_arr else None, arr)
    filtered_arr.sort()
    print filtered_arr[-2]