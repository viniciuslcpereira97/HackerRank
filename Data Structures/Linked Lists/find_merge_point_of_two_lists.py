#!usr/bin/env python
#-*- coding: utf-8 -*-

"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
"""
 
class Node(object):
 
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def FindMergeNode(headA, headB):
    checker = dict()
    while headA:
        checker[headA.data] = 0
        headA = headA.next
    
    while headB:
        if checker.has_key(headB.data):
            return headB.data
        else:
            headB = headB.next