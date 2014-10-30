#!/usr/bin/env python

## List Comprehension

## Structure:
## [ <term> <for> (optional <for> or <if>)]

## Any number of optional clauses (for, if)

## Read Left to Right except the Term which is read last.

## Term is defined in the clauses.

## uses square brackets

statement = [('what','1'),('good','2')]

##result = []
##for a,b in statement:
##    if a in ['good','bad','ugly']:
##        result.append(b)
##

result = [b for a,b in statement if a in ['good','bad','ugly']]

print result
