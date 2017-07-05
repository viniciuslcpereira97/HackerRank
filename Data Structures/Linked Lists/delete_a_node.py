#!usr/bin/env python
#-*- coding: utf-8 -*-

"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 return back the head of the linked list in the below method. 
"""
class Node(object):
 
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def Delete(head, position):
    if position == 0:
        return head.next
    else:
        temp = head
        count = 0
        while count < position - 1:
            temp = temp.next
            count = count + 1
        
        delnode = temp.next
        temp.next = temp.next.next
        delnode.next = None
        return head