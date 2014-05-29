#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" chap11ex2.py - Chapter 11, Exercise 2 """

def fact(number):
    """ computes the factorial of a number """
    product = 1
    for i in range(1, number+1):
        product *= i
    return product

print 'Enter a number: '
NUM = int(input())
print str(NUM) + '! equals ' + str(fact(NUM))
