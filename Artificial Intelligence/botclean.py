#!/usr/bin/python
moves = { "X": {"POS": "LEFT", "NEG": "RIGHT"}, "Y": {"POS": "DOWN", "NEG": "UP"}}

def update_board(bot_coord, dirty_coord, board):
    board[bot_coord[0]][bot_coord[1]] = '-'
    board[dirty_coord[0]][dirty_coord[1]] = 'b'

def get_move(bot_coord, dirty_coord):
    global moves
    x_sub = bot_coord[0] - dirty_coord[0]
    y_sub = bot_coord[1] - dirty_coord[1]
    if x_sub != 0:
        move = moves["X"]["NEG"] if x_sub < 0 else moves["X"]["POS"]
    if y_sub != 0:
        move = moves["Y"]["NEG"] if y_sub < 0 else moves["Y"]["POS"]
    return move

def next_move(posr, posc, board):
    for n, x in enumerate(board):
        if 'd' in x:
            bot_cell, dirty_cell = (posr, posc), (x.index('d'), n)
            next_move = get_move(bot_cell, dirty_cell)
            update_board(bot_cell, dirty_cell, board)
            return next_move

if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
