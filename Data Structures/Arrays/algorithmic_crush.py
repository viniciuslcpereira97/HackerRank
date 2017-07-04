#!usr/bin/env python
#-*- coding: utf-8 -*-

f_input = raw_input().split()
arr_len = int( f_input[0] )
n_operations = int( f_input[1] )

values = {}

for n in range(0, arr_len):
    values[str(n)] = 0

for n in range(0, n_operations):
    o_input = raw_input().split()
    for x in range(int(o_input[0]) - 1 , int(o_input[1]) ):
        values[str(x)] += int(o_input[2])

return_values = [values[x] for x in values]
return_values.sort()

print return_values[-1]