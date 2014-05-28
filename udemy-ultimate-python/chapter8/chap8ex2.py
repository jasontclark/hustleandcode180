#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Chapter 8, Exercise 2 """
BAR = ''
for grade in open('grades.txt'):
    for i in range(1, int(grade) + 1):
        if i % 5 == 0:
            BAR = BAR + '*'
    print(BAR, i)
    BAR = ''
