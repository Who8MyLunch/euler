
from __future__ import division, print_function, unicode_literals


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


if __name__ == '__main__':

    # Setup.
    value = 600851475143
    # value = 8462696833
    # value = 13195

    # Do it.
    for v in find_factors(value):
        print(v)

    # Done.

