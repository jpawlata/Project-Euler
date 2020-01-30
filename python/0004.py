# Author: Justyna Pawlata
# Project Euler (https://projecteuler.net/)

# Problem 4:
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome(number):
    number = str(number)
    digits_num = len(number)
    if digits_num % 2 != 0: return False
    elif number[:int(digits_num/2)] == number[int(digits_num/2):][::-1]: return True
    else: return False

def two_3_digit_numbers(number_one, number_two):
    return number_one * number_two

first_3_digit = 100
last_3_digit = 999
palindrme_list = []

for i in range(first_3_digit, last_3_digit+1):
    for y in range(first_3_digit, last_3_digit+1):
        result = two_3_digit_numbers(i, y)
        if palindrome(result):
            palindrme_list.append(result)

palindrme_list.sort()
answer = palindrme_list[-1]
print(answer)