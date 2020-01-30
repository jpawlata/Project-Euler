# Author: Justyna Pawlata
# Project Euler (https://projecteuler.net/)

# Problem 3:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# check if the number is prime
def prime_num(num):
    if num <= 1:
        return False
    else:
        for i in range(2, ((num//2)+1)):
            if num % i == 0:
                return False
    return True


# list all prime factors of the given number
def prime_factors(number):
    prime_list = []
    for i in range(2, int((number + 1)**0.5)):
        # if modulo is equal to 1 and prime_num is True
        if (number % i) == 0 and prime_num(i):
            prime_list.append(i)
    return prime_list


given_number = 600851475143
# only largest prime factor as an answer
answer = prime_factors(given_number)[-1]
print(answer)

            
