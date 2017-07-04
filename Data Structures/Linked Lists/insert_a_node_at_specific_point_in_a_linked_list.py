#!usr/bin/env python
#-*- coding: utf-8 -*-

"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 return back the head of the linked list in the below method. 
"""
class Node(object): 
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# If list is empty, returns list with given data
# If position to insert data is 0, insert at head of the list
# Else, iterate through the values and insert data at given position
def InsertNth(head, data, position):
    if not head:
        return Node(data)
    if position == 0:
        return Node(data, head)
    else:
        current = head
        for _ in range(position - 1):
            current = current.next
        current.next = Node(data, current.next)
        return head