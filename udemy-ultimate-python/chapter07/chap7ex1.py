#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" chap7ex1.py - udemy chapter 7, exercise 1 """
TRIES = 0
ANSWER = 'Watson'
while TRIES <= 3:
    TRIES = TRIES + 1
    print 'What is the name of the computer that played on Jeopardy?'
    RESPONSE = raw_input()
    if RESPONSE == 'Watson':
        print 'That is right!'
        break
    elif TRIES == 3:
        print 'Sorry. The answer is Watson'
        break
    else:
        print 'Sorry. Try again.'
