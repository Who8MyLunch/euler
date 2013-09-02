
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

Only work with odd numbers, except for 5.  Any number ending in five is divisible by 5 and tus not a prime.

"""

import numpy as np

# Helpers.
def prime_factor(z):
    """
    Search for first prime factor of the input value.
    """

    a = int(z**.5)

    for i in [2, 3, 5, 7]:
        if i >= z:
            break

        if z / i % 1 == 0:
            return i


    for i in range(11, a, 10):
        # 11
        if z / i % 1 == 0:
            return i

        # 13
        if z / (i+2) % 1 == 0:
            return i

        # 17
        if z / (i+6) % 1 == 0:
            return i

        # 19
        if z / (i+8) % 1 == 0:
            return i

    # If we get this far then z must be a prime.
    return None

#################################################


# Setup.
value = 600851475143

# Do it.
# while True:




# print('\nThe answer: {:d}'.format(answer))

# Done.
