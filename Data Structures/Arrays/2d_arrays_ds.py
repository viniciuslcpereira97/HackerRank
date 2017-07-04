#!/bin/python

import sys

arr = []
# Get all user input
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

# Initializes sums variable
sums = list()

# Sum all hourglasses and insert in a list
# O(n²)
for x, row in enumerate(arr[:-2]):
    for y, item in enumerate(row[:-2]):
        f_row = item + row[y + 1] + row[y + 2]
        s_row = arr[x + 1][y + 1]
        t_row = sum( arr[x + 2][y : y+3] )
        sums.append( f_row + s_row + t_row )
sums.sort()
print sums[-1]