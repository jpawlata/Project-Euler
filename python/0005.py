# Author: Justyna Pawlata
# Project Euler (https://projecteuler.net/)

# Problem 5:
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def divByNum1_20(number):
    for i in range(11, 20+1):
        if number % i != 0:
            return False
    return True

def smallestDivBy1_20(number, incr):
    while True:
        if divByNum1_20(number) is False:
            number += add_num
        else:
            return number

start = 2520
add_num = 20

answer = smallestDivBy1_20(start, add_num)
print(answer)
