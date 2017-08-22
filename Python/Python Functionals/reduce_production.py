#!usr/bin/env python
#-*- coding: utf-8 -*-
from __future__ import print_function
from fractions import Fraction

def product(fracs):
    t = reduce(lambda x, y: Fraction(x, y), fracs, 1)
    return t.denominator, t.numerator

if __name__ == '__main__':
    fracs = []
    for _ in range(input()):
        fracs.append(Fraction(*map(int, raw_input().split())))
    result = product(fracs)
    print(*result)