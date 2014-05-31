#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" sphere.py - Chapter 14, Exercise 1 """
PI = 3.1459

def area(radius):
    """
    compute the area
    """
    return 4 * PI * (radius * radius)

def volume(radius):
    """
    computer the volume
    """
    return (4.0/3.0) * PI * (radius * radius * radius)
