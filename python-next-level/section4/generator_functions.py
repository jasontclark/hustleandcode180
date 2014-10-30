#!/usr/bin/env python
""" Section 4, Lecture 44 - Generator Functions """

def count(start,end):
    i = start
    while i <= end:
        yield i
        i = i+1

c = count(0,10)

print c
print c.next()
print c.next()
print c.next()

for i in c:
    print i

def count_again(start, end = None):
    i = start
    while i <= end or end == None:
            yield i
            yield -i
            i = i+1

d = count_again(0)
print d

for i in range(100):
    print d.next()
