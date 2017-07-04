#!usr/bin/env python
#-*- coding: utf-8 -*-

"""
 Print elements of a linked list on console
 head input could be None as well for empty list
 Node is defined as
"""

# For each value at linked list print data and update head to next value
def print_list(head):
    while head != None:
        print head.data
        head = head.next

class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node