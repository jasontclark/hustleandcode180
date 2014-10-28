#!/usr/bin/env python
""" Section 4, Lecture 43 - Generator Expressions """

g = (x*x for x in range(10))

l = [x*x for x in range(10)]

for i in g:
    print i
