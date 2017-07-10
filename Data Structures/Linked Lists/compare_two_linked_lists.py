#!usr/bin/env python
#-*- coding: utf-8 -*-

"""
 Compare two linked list
 head could be None as well for empty list
 Node is defined as
 return back the head of the linked list in the below method.
"""
class Node(object):
 
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def CompareLenght(headA, headB):
    while headA.next != None and headB.next !=None:
        headA = headA.next
        headB = headB.next
    return int( headA.next == None and headB.next == None )

def CompareLists(headA, headB):
    if CompareLenght(headA, headB):
        while headA != None and headB != None:
            if headA.data == headB.data:
                headA = headA.next            
                headB = headB.next
            else:
                return int(False)           
        return int(True)
    else:
        return int(False)

headA = Node(1, Node(2, Node(3)))
headB = Node(1, Node(2))

print CompareLists(headA, headB)