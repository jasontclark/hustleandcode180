#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" activity.py - udemy chapter 6, exercise 2 """

MESSAGE = 'The recommended activity is '
print 'Enter the temperature: '
TEMP = int(raw_input())

if TEMP > 85:
    MESSAGE = MESSAGE + 'swimming.'
elif TEMP >= 70:
    MESSAGE = MESSAGE + 'tennis.'
elif TEMP >= 32:
    MESSAGE = MESSAGE + 'golf.'
elif TEMP >= 0:
    MESSAGE = MESSAGE + 'dancing.'
else:
    MESSAGE = MESSAGE + 'sitting by the fire.'

print MESSAGE
