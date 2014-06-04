#!/usr/bin/env python
""" Russian Peasant's Algorithm """

# Input two numbers
print 'Enter first number: '
num1 = int(input())

print 'Enter second number: '
num2 = int(input())

def russian(num1, num2):
    if num1 > 1:
          num1 = num1 / 2
          num2 = num2 * 2
          print str(num1) + ' ' + str(num2)

    russian(num1, num2)
