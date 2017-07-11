#!usr/bin/env python
#-*- coding: utf-8 -*-
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
 return back the node data of the linked list in the below method.
"""
 
class Node(object): 
    
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def CountNodes(head):
    counter = 0
    while head is not None:
        counter = counter + 1
        head = head.next
    return counter

def GetNode(head, position, curr=None):
    curr = ( CountNodes(head) - 1 )
    print "curr: {} --> position: {} --> value: {}".format(curr, position, head.data)
    if curr == position:
        return head.data
    else:
        if head.next is not None:
            return GetNode(head.next, position, (curr - 1))


head = Node(1, Node(2, Node(3, Node(4))))
print GetNode(head, 4)