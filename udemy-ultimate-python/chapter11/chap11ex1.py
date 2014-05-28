#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" chap11ex1.py - Chapter 11, Exercise 1 """

def tax(amount):
    """ computes the tax amt """
    if amount <= 240:
        return 0
    elif amount > 240 and amount <= 480:
        return amount * .15
    else:
        return amount * .28

def netpay(grosspay):
    """ computes the netpay """
    return grosspay - tax(grosspay)

print 'Enter gross pay: '
GROSS = int(input())
print 'Net pay is ' + str(netpay(GROSS))
