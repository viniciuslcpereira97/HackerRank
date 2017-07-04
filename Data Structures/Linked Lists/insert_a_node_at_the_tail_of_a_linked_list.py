#!usr/bin/env python
#-*- coding: utf-8 -*-

"""
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
    Class
 return back the head of the linked list in the below method
"""
 
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def Insert(head, data):
    if not head:
        return Node(data)
    if head.next != None:
        Insert(head.next, data)
    else:
        head.next = Node(data)
    return head
