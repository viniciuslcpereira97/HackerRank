#!usr/bin/env python
#-*- coding: utf-8 -*-

def getCommand(r, c, prin_y, prin_x):
    if prin_y != c:
        return "LEFT" if prin_y < c else "RIGHT"
    if prin_x != r:
        return "UP" if prin_x < r else "DOWN"

def getPrincessLocation(grid):
    for x, i in enumerate(grid):
        if 'p' in i:
            return (x, i.index('p'))

def nextMove(n,r,c,grid):
    prin_x, prin_y = getPrincessLocation(grid)
    # (prin_x = 2, prin_y = 0)
    return getCommand(r, c, prin_y, prin_x)

n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(list(raw_input()))

print nextMove(n,r,c,grid)
