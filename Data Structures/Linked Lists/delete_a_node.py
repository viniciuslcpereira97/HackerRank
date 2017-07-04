#!usr/bin/env python
#-*- coding: utf-8 -*-

"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 return back the head of the linked list in the below method. 
"""
def print_list(head):
    while head != None:
        print head.data
        head = head.next

class Node(object):
 
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def Delete(head, position):
    if position == 0:
        return head.next
    else:
        prevNode = head
        for _ in range(position - 1):
            prevNode = head.next

        delete_node = prevNode.next
        posNode = delete_node.next
        prevNode.next = posNode
        return head

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))

head = Delete(head, 4)

print_list(head)