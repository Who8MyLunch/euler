
from __future__ import division, print_function #, unicode_literals

"""
Largest palindrome product


A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.



"""

import numpy as np

# Helpers.
def separate_digits(v):
    """
    separate number into a list of digit values.
    """
    d = []
    while True:
        d.append(v % 10)
        v = int(v / 10)

        if v < 1:
            break

    return d[::-1]



def is_palindromic(value):
    """
    Test to see if supplied value is palindromic.
    """

    digits = separate_digits(value)

    flag = True
    for i in range(int(len(digits)/2)):
        a = digits[i]
        b = digits[-i-1]
        val = a == b

        flag = flag and val

    return flag



#############################

vmin = 100
vmax = 999

# Do it.
zmax = 0

for i in range(vmin, vmax+1):
    for j in range(i, vmax+1):
        z = i*j
        if is_palindromic(z):
            if z > zmax:
                print(i, j, z)
                zmax = z
                ijmax = i, j

# Done.
