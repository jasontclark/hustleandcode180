#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" listcomp.py - quick example of using list comprehensions - Chapter 10, Exercise 1 """
N = range(1,101)
EN = [x for x in N if x % 2 == 0]
print EN
