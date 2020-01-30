# Author: Justyna Pawlata
# Project Euler (https://projecteuler.net/)

# Problem 6:
# The sum of the squares of the first ten natural numbers is,
# 12+22+...+102=385
# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)2=552=3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


# natural numbers > 0 (1, 2, 3, 4 ... )

def sumOfSquares(number):
    result = 0
    for i in range(1, number+1):
        result += i**2
    return result

def squareOfSum(number):
    result, temp = 0, 0
    for i in range(1, number+1):
        temp += i
    result = temp**2
    return result
        
number = 100
# absolute value of the difference
answer = abs(sumOfSquares(number) - squareOfSum(number))
print(answer)
