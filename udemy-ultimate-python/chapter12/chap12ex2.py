#!/usr/bin/env python
""" chap12ext.py - Chapter 12, Exercise 2 """

def first(word):
    """ grab the first letter of the word """
    return word[0]

def get_acronym(words):
    """
    map the first function the the list WORDS. A list is returned.
    then to output a string, use join to add the list items to the ACRO
    string. then run upper to make the string in all uppercase.
    """
    acro = ''
    acro = acro.join(list(map(first, words))).upper()
    return acro

WORDS = ['in', 'my', 'humble', 'opinion']

ACRO = get_acronym(WORDS)

print ACRO
