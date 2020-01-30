# Author: Justyna Pawlata
# Project Euler (https://projecteuler.net/)

# Problem 7:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# check if the number is prime (taken from problem no. 3)
def ifPrime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, ((num//2)+1)):
            if num % i == 0:
                return False
    return True

def primeNumList(limit):
    prime_list = []
    for i in range(2, 10000000):
        if ifPrime(i): prime_list.append(i)
        if len(prime_list) == limit: 
            return prime_list
                
limit = 10001

prime_list = primeNumList(limit)
print(prime_list[-1])