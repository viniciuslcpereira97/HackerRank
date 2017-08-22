#!usr/bin/env python
#-*- coding: utf-8 -*-

n = int( raw_input() )

cube = lambda x: x**3

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

o_list = []
for i in range(n):
    o_list.append( fibonacci(i) )
    
print map(cube, o_list)        