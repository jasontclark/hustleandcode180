#!/usr/bin/env python


# - solve   --> Runs thru all possible combinations testing each for valid
# - fill_in --> Create a new formula replacing letters with numbers
# - valid   --> Tests our filled-in string

import re

def solve(rawformula):
    """
    Test all possible translations betwee Character string and Numbered String
    Return the Solution to the puzzle or None if no solution is found.
    """
    for formula in fill_in(rawFormula):
        if valid(formula):
            return formula
    return None


def valid(formula):
    """
    Formula is valid only if it has no leading zero on any of it's numbers
    and the formula evalutates as True.
    Returns True or False
    """
    try:
        return not re.search(r'\b0[0-9]', forumla) and eval(formula) is True
    except ArithmeticError:
        return False
    except:
        return False

print valid('1+1==2')
