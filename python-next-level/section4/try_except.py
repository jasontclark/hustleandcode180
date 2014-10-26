#!/usr/bin/env python

# Try
# Except

userDefined = 'b'

try:
    a = int(userDefined)
except ValueError:
    a = int(1)
except Exception:
    a = int(0)
finally:
    print a
