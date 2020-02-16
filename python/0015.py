# Author: Justyna Pawlata
# Project Euler (https://projecteuler.net/)

# Problem 15:
# Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.
# How many routes are there through a 20x20 grid?

from math import factorial

def count_routes(i, y):
    return factorial(i)/(factorial(y)*factorial(i-y))

answer = int(count_routes(20*2, 20))
print(answer)