#!/usr/bin/env python
# -*- coding: utf8 -*-
""" test.py - Tests for brandywine """
import os
from brandywine import *

# create the brandywine object
brw = BrandyWine(os.environ.get('ROTTEN_API_KEY'))

# return the list directory json
jsonlist = brw.return_list_directory_json()
print jsonlist

movieslist = brw.return_movies_list_json()
print movieslist
