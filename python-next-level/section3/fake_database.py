#!/usr/bin/env python
""" Russian Peasant's Algorithm """
import time

def russian(num1, num2):
    x = num1; y = num2    ## Compound Assignment
    z = 0                 ## Acumulator

    while x > 0:          ## While Loop Begins
        if x % 2 == 1:    ## Modulo operator
            z = z + y     ## Acumulate Sum
        y = y << 1        ## Shift Binary Left
        x = x >> 1        ## Shift Binary Right
    return z              ## Return Z

def test_russian():
    start_time = time.time()
    print russian(357, 16)
    print 'Russian Algorithm took %f seconds' % (time.time() - start_time)

    assert russian(357, 16) == 5712

if __name__ == "__main__":
    test_russian()
