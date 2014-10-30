#!/usr/bin/env python
""" re_search.py - searches a string for a leading zero."""
import re

def noFirstZero(formula):
    """ uses a regular expression search to look for a leading zero. """
    return not re.search(r'\b0[0-9]', formula)

def test_noFirstZero(L):
    """ runs a quick test. """
    for formula in L:
        print formula, noFirstZero(formula)

""" Test """
L = ['123', '406', '023', '543 0543', '087 65', '00', '432 123']
test_noFirstZero(L)
