#!usr/bin/env python
#-*- coding: utf-8 -*-

u_input = raw_input().split()
arr_input = raw_input()
arr_len = int( u_input[0] )
arr_rot = int( u_input[1] )

arr = arr_input.split()
new_arr = [None] * arr_len

# O(n)

for x, i in enumerate(arr):
    rotation = ( x - arr_rot ) if ( x - arr_rot ) >= 0 else ((arr_len) + (x - arr_rot)) 
    new_arr[rotation] = i

print " ".join(str(item) for item in new_arr)