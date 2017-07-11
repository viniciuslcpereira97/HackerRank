#!usr/bin/env python
#-*- coding: utf-8 -*-

"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 return back the head of the linked list in the below method.
"""
 
class Node(object):
 
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def RemoveDuplicates(head):
    if head.next is not None: 
        if head.next.data == head.data:
            head.next = head.next.next
            RemoveDuplicates(head)
            return head 
        else:
            RemoveDuplicates(head.next)
            return head 
    else:
        return head