# Author: Justyna Pawlata
# Project Euler (https://projecteuler.net/)

# Problem 20:
# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

import math

def sum_of_digits(number):
    sum_fact = 0
    fact = math.factorial(number)
    for digit in str(fact):
        sum_fact += int(digit)
    return sum_fact

number = 100
answer = sum_of_digits(number)
print(answer)