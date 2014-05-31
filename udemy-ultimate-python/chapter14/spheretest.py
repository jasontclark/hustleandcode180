#!/usr/bin/env python
# -*- coding: utf8 -*-
""" spheretest.py - Chapter 14, exercise 1 """
#from sphere import *
import sphere

print 'Enter the radius :'
radius = int(input())

print 'The area is: ' + str(sphere.area(radius))
print 'The volume is: ' + str(sphere.volume(radius))
