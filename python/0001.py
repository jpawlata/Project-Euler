# Author: Justyna Pawlata
# Project Euler (https://projecteuler.net/)


# Problem 1:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def multiples_3_5(limit):
    # natural numbers: from 1
    for number in range(1, limit):
        if (number % 3 == 0) or (number % 5 == 0):
            numbers.append(number)
    return numbers


limit = 1000
numbers = []

num = multiples_3_5(limit)

# sum of all numbers
answer = sum(num)
print(answer)