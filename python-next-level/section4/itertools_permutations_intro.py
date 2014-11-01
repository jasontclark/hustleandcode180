#!/usr/bin/env python

import itertools

letters = 'AF'
perms = itertools.permutations('123', len(letters))

print perms
for perm in perms:
    print perm
