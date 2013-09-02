
from __future__ import division, print_function, unicode_literals

"""
Largest prime factor
====================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?


Notes
=====

I have an idea, but I think it will be more brute force than elegant.

Set value to the big number

Decrement

Check if this number is divisble into the big number.

Only work with odd numbers, except for 5.  Any number ending in five is
divisible by 5 and tus not a prime.



Two parts to the problem.
1. Determine if a number is a prime number.
2. Find the factors of a number.

"""

import numpy as np

# Helpers.
def first_factors(z):
    """
    Search for first factor of the input value.
    """
    values_init = [2, 3, 5, 7, 9]
    for v in values_init:
        if v >= z:
            # If we get here then value z must be a prime.
            return None

        w = z / v
        if w % 1 == 0:
            # Found a factor.
            return v

    # Keep searching.
    value_end = int(z**.5)
    for i in xrange(10, value_end, 10):

        # 11
        v = i + 1
        w = z / v
        if w % 1 == 0:
            return v

        # 13
        v = i + 3
        w = z / v
        if w % 1 == 0:
            return v

        # 17
        v = i + 7
        w = z / v
        if w % 1 == 0:
            return v

        # 19
        v = i + 9
        w = z / v
        if w % 1 == 0:
            return v


    return None



def find_factors(z):
    """
    Search for all factors of input value.

    This is a generator.
    """
    while True:
        a = first_factors(z)

        if a:
            # print(a)
            yield a
            z = int(z / a)
        else:
            # print(z)
            yield z
            break

#################################################


# Setup.
value = 600851475143
# value = 8462696833
# value = 13195

# Do it.
for v in find_factors(value):
    print(v)

# Done.
