"""
 Insert Node at the begining of a linked list
 head input could be None as well for empty list
 Node is defined as
 
 return back the head of the linked list in the below method. 
"""

class Node(object):
 
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# If linked list is empty, creates a Node with given data
# Else, swap values from current to next
def Insert(head, data):
    if head == None:
        return Node(data)
    else:
        new_node = Node(data)
        new_node.next = head
        head = new_node
    return head