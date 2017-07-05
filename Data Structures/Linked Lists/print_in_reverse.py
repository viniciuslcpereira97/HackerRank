#!usr/bin/env python
#-*- coding: utf-8 -*-

"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
"""
def print_list(head):
    while head != None:
        print head.data
        head = head.next

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def ReversePrint(head):
    if head == None:
        return
    else:
        ReversePrint(head.next)
        print head.data        

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))

ReversePrint(head)