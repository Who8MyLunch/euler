
from __future__ import division, print_function #, unicode_literals

"""
Problem 5: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without
any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers
from 1 to 20?
"""

import numpy as np
import scipy as sp
import scipy.misc

import utility

# Helpers.



# Setup.
number = 20

value = sp.misc.factorial(number, exact=True)

for k in range(number, 1, -1):
    f = [v for v in utility.find_factors(k)]
    print(f)





# Do it.



# print('\nThe answer: {:d}'.format(answer))

# Done.
