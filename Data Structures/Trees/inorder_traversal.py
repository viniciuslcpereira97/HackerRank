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
        
def inOrder(root):
    if not root:
        return
    if root:
        inOrder(root.left)
        print root.data,
        inOrder(root.right)

inOrder(head)