#!/usr/bin/env python
""" execptex1.py - chapter 17, exercise 1 """

def calc(op1, op2, op):
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2

CONT = 'y'
while CONT != 'n':
    print 'Enter the first number: '
    num1 = int(input())
    print 'Enter the second number: '
    num2 = int(input())
    print 'Enter operation: '
    op = input()
    if op == '/' and num2 == 0:
        print 'Cannot divide by zero.'
        continue
    else:
        print str(calc(num1, num2, op))
    print 'Do you want to continue (y/n) '
    CONT = input()
