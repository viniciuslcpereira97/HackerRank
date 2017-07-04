"""
 Insert Node at the begining of a linked list
 head input could be None as well for empty list
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

def Insert(head, data):
    if head == None:
        return Node(data)
    else:
        new_node = Node(data)
        new_node.next = head
        head = new_node
    return head

head = Node(1, Node(2))
head = Insert(head, 3)

print_list(head)
