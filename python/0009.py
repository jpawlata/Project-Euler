# Author: Justyna Pawlata
# Project Euler (https://projecteuler.net/)

# Problem 9:
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from functools import reduce

number = 1000
def tripletPyth():
    values = []
    for a in range(1, number):
        for b in range(1, number):
            if (a < b) and (a + b + (a**2 + b**2)**0.5 == number):
                c = number - (a + b)
                values.extend([a, b, c])
    return values

answer = reduce((lambda x, y: int(x) * int(y)), tripletPyth())
print(answer)