#!usr/bin/env python
#-*- coding: utf-8 -*-

"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 return back the head of the linked list in the below method. 
"""

def print_list(head):
    while head != None:
        print head.data
        head = head.next
 
class Node(object): 
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def InsertNth(head, data, position):
    if position == 0:
        return Node(data, head)
    else:
        current = head
        for _ in range(position - 1):
            current = current.next
        current.next = Node(data, current.next)
        return head

head = Node(55, Node(66, Node(77, Node(88, Node(99)))))

head = InsertNth(head, 111, 3)

print_list(head)