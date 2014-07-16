#!/usr/bin/env python

import string

enc_table = string.maketrans('ABCDEF', '123456')
dec_table = string.maketrans('123456', 'ABCDEF')

enc = 'BED FACED'.translate(enc_table)

print enc

dec = enc.translate(dec_table)

print dec
