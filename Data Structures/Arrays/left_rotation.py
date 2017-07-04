#!usr/bin/env python
#-*- coding: utf-8 -*-

# User inputs
u_input = raw_input().split()
arr_input = raw_input()

# Parses user inputs
arr_len = int( u_input[0] )
arr_rot = int( u_input[1] )

# Get array values
arr = arr_input.split()

# Creates empty array
new_arr = [None] * arr_len

# Checks value of new index to each value
# Rotates each value to new index
# O(n)
for x, i in enumerate(arr):
    rotation = ( x - arr_rot ) if ( x - arr_rot ) >= 0 else ((arr_len) + (x - arr_rot)) 
    new_arr[rotation] = i

print " ".join(str(item) for item in new_arr)