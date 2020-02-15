# Author: Justyna Pawlata
# Project Euler (https://projecteuler.net/)

# Problem 10:
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def prime_num(num):
    if num <= 1:
        return False
    else:
        for i in range(2, ((num//2)+1)):
            if num % i == 0:
                return False
    return True


def sumOfPrimes(limit):
    result = 0
    for i in range(2, limit):
        if prime_num(i):
            result += i 
            print(i, result)
    return result

limit = 2000000
answer = sumOfPrimes(limit)
print(answer)