#!/usr/bin/env python

## enumerate(sequence)

##      Return an enumerate object. sequence must be a sequence, an iterator,
##      or some other object which supports iteration. The next() method of the
##      iterator returned by enumerate() returns a tuple containing a count
##      (from start which defaults to 0) and the values obtained from iterating
##      over sequence:

for (i, d) in enumerate("ONE"):
    print (i,d)
    print '{}*{}'.format(10**i, d)
    print ""
