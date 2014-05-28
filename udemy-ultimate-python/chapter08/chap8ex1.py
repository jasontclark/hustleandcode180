#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Chapter 8, Exercise 1 """
print 'Enter a number: '
NUM = int(input())
FACT = 1

for i in range(1, NUM+1):
    FACT = FACT * i
print str(NUM) + '! = ' + str(FACT)
