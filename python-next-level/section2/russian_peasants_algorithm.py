#!/usr/bin/env python
""" Russian Peasant's Algorithm """

def russian(num1, num2):
    x = num1; y = num2
    z = 0

    while x > 0:
        if x % 2 == 1:
            z = z + y

        # Binary Shifting: << shifts left, >> shifts right
        y = y << 1
        x = x >> 1

    return z

print russian(24,16)
print russian(357,16)
