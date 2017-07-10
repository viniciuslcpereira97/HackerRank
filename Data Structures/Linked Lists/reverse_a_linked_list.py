#!usr/bin/env python
#-*- coding: utf-8 -*-

"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 return back the head of the linked list in the below method.
"""
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def Reverse(head, prev=None):
    if head.next is not None:
        rev = Reverse(head.next, head)
        head.next = prev
        return rev
        
    head.next = prev
    return head
