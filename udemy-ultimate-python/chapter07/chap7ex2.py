#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" chap7ex2.py - udemy chapter 7, exercise 2 """

OP1 = 0.0
OP2 = 0.0
OP = ''

while OP1 != 'q':
    print 'Enter first number (q to quit): '
    OP1 = raw_input()
    if OP1 == 'q':
        break
    OP1 = float(OP1)
    print 'Enter second number: '
    OP2 = float(raw_input())
    print 'Enter an operation (+,-,*,/): '
    OP = raw_input()
    if OP == '+':
        print OP1 + OP2
    elif OP == '-':
        print OP1 - OP2
    elif OP == '*':
        print OP1 * OP2
    elif OP == '/':
        print OP1 / OP2
    else:
        print 'Did not recognize operator.'
