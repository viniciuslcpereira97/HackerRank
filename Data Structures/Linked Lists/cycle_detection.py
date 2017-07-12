#!usr/bin/env python
#-*- coding: utf-8 -*-

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:  
"""
 
class Node(object):
 
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def has_cycle(head):
    if not head.next:
        return 0
    if head.next.next == head:
        return 1
    has_cycle(head.next)