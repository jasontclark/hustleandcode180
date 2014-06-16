#!/usr/bin/env python
""" takedrop.py - chapter 18 exercise """

def take(num, lyst):
    rlist = []
    for i in range(0, num):
        rlist.append(lyst[i])
    return rlist

def drop(num, lyst):
    rlist = []
    for i in range(num, len(lyst)):
      rlist.append(lyst[i])
    return rlist

names = ['Raymond', 'Cynthia', 'David', 'Jennifer', 'Clayton']
somenames = take(3, names)
print(somenames)
somenames = drop(3, names)
print(somenames)
