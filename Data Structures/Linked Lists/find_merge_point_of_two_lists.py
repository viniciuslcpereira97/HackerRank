#!usr/bin/env python
#-*- coding: utf-8 -*-

from print_the_elements_of_a_linked_list import print_list

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

headA = Node(2, Node(4, Node(3, Node(7))))
headB = Node(6, Node(11, Node(5, Node(3, Node(7)))))
print FindMergeNode(headA, headB)
""" TEST CASE
    2-4-3-5-7 --> 6-11-3-5-7
    2-4-3-7 --> 6-11-5-3-7
    2-4-7 --> 6-11-5-3-7
"""