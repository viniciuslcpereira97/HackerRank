#!usr/bin/env python
#-*- coding: utf-8 -*-

if __name__ == '__main__':
    N = int(raw_input())

    final_list = list()

    for _ in range(N):
        input = raw_input().split()
        command = input[0]
        args = "({})".format(", ".join(input[1:])) if len(input) > 1 else "()"
        if command == 'print':
            print(final_list)
        else:
            exec_function = 'final_list.{}{}'.format(command, args) 
            eval(exec_function)