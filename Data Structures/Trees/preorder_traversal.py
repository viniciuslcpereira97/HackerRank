#!usr/bin/env python
#-*- coding: utf-8 -*-

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

class Node(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n1.right = n2
n2.right = n5
n5.left = n3
n3.right = n4
n4.right = n6
empty_head = n1

def preOrder(root):
    if not root:
        return
    print root.data,
    preOrder(root.left)
    preOrder(root.right)

preOrder(empty_head)