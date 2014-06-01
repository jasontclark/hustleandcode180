#!/usr/bin/env python
# -*- coding: utf8 -*-
""" test.py - Tests for brandywine """
import os
from brandywine import *

brwine = BrandyWine(os.environ.get('ROTTEN_API_KEY'))
url = brwine.getApiUrl()

print url
