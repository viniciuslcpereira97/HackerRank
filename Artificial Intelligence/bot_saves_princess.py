#!usr/bin/env python
#-*- coding: utf-8 -*-

moves = {
    "X" : {"POS": "UP", "NEG": "DOWN"},
    "Y" : {"POS": "LEFT", "NEG": "RIGHT"} 
}

def drawGrid():
    m = input()
    grid = []
    
    for i in xrange(0, m):
        grid.append( list(raw_input()) )

    return grid

def getEntitiesPosition(grid):
    bot_pos = (len(grid) - 1) / 2
    bot_pos = (bot_pos, bot_pos)

    for n, x in enumerate(grid):
         if 'p' in x:
            peach = (n, x.index('p'))

    return [bot_pos, peach]

def getCommand(n1, n2, axis):
    global moves
    sub = "NEU"
    command_num = n1 - n2
    commands = []
    if n1 < n2:
        sub = "NEG"
        command_num = command_num * -1
    elif n1 > n2:
        sub = "POS"

    for x in range(0, command_num):
        commands.append( moves[axis][sub] )

    return commands


def displayPathtoPrincess(positions):
    x1, y1 = positions[0]
    x2, y2 = positions[1]
    x_commands, y_commands  = getCommand(x1, x2, "X"),  getCommand(y1, y2, "Y") 
    all_commands = x_commands + y_commands
    print "\n".join(all_commands)

grid = drawGrid()
positions = getEntitiesPosition(grid)
displayPathtoPrincess(positions)