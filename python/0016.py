# Author: Justyna Pawlata
# Project Euler (https://projecteuler.net/)

# Problem 16:
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

def power(number, power):
    return number ** power

def sum_of_digits(num, pow):
    digits = power(num, pow)
    return sum(map(int, str(digits)))

answer = sum_of_digits(2, 1000)
print(answer)