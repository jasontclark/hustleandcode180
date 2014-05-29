#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Chapter 12, Exercise 1 """

def countLetters(words):
    """ recursive function that counts the number of letters in a sentence """
    if len(words) < 1:
        return False
    else:
        return len(words[0]) + countLetters(words[1:])

SENTENCE = ['now', 'is', 'the', 'time', 'for', 'all', 'good', 'people']
print SENTENCE
print countLetters(SENTENCE)
