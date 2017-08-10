#!usr/bin/env python
#-*- coding: utf-8 -*-

class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None            

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n3.left = n2
n3.right = n5
n2.left = n1
n5.left = n4
n5.right = n6
n6.right = n7

def height(root):
    if not root:
        return
    if root:
        print root.info
        height(root.left)
        print "change"
        height(root.right)

height(n3)