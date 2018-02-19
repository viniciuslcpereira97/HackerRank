#!usr/env/python
#-*- coding: utf-8 -*-

from collections import defaultdict

restaurant_dict = defaultdict(dict)

class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def next(next):
        self.next = next

def addRestaurant(restaurant_name):
    node = Node('b', Node('a', Node('r', Node(' ', Node('d', Node('o', Node(' ', Node('z', Node('e', Node())))))))))
    while node.next:
        print node.value
        node = node.next

def getRestaurant(restaurant_name):
    return restaurant_name

def main():
    addRestaurant("bar do ze")
    getRestaurant("teste")

if __name__ == "__main__":
    main()
