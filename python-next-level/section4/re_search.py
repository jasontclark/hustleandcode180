#!/usr/bin/env python

import re

def noFirstZero(formula):
    return not re.search(r'\b0[0-9]', formula)

def test_noFirstZero(L):
    for formula in L:
        print formula, noFirstZero(formula)

L = ['123', '406', '023', '543 0543', '087 65', '00', '432 123']
test_noFirstZero(L)
