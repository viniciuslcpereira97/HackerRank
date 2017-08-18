#!usr/bin/env python
#-*- coding: utf-8 -*-

import json

class Trie(object):

    def __init__(self):
        self.root = {}
        self.__end = '__end__'

    def insert(self, word):
        trie = self.root
        current_dict = trie
        for let in word:
            current_dict = current_dict.setdefault(let, {})
        current_dict[self.__end] = self.__end

    def countSimilars(self, partial):
        trie = self.root
        current_dict = trie
        accumulator = 0
        for let in partial:
            current_dict = current_dict[let]
        # len(current_dict[iterator.next()])
        # while current_dict.keys():
            # current_dict = current_dict[current_dict.keys()[0]]
        return json.dumps(trie, indent=4)

    def check(self):
        print self.root

myTrie = Trie()

names = [
    'abc',
    'abcd',
    'abcde',
    'aceg',
    'acfp',
    'adef',
]

for name in names:
    myTrie.insert(name)

# myTrie.check()
print myTrie.countSimilars('ab')