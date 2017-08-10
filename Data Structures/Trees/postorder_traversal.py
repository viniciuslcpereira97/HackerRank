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
        
def postOrder(root):
    if not root:
        return
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print root.data,

postOrder(head)