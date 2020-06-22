# Author: Justyna Pawlata
# Project Euler (https://projecteuler.net/)

# Problem 17:
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


numbers = {
    0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 
    18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
    80: "eighty", 90: "ninety", 100: "one hundred", 200: "two hundred", 300: "three hundred", 400: "four hundred", 
    500: "five hundred", 600: "six hundred", 700: "seven hundred", 800: "eight hundred", 900: "nine hundred", 1000: "one thousand"
}

start_num = 1
final_num = 1000
len_and = len("and")

def letters_total(start_num, final_num):
    letters_num = 0
    for i in range(start_num, final_num + 1):
        if (i > 0 and i <= 20):
            letters_num = letters_num + len(numbers[i])
        elif (i > 20 and i < 100):
            number_1 = int(str(i)[0] + str(0))
            number_2 = int(str(i)[1])
            
            if number_2 == 0:
                letters_num = letters_num + len(numbers[number_1])
            else:
                letters_num = letters_num + len(numbers[number_1]) + len(numbers[number_2])
        elif i == 1000:
            letters_num = letters_num + len(numbers[i]) - 1
        else:
            number_0 = int(str(i)[0] + str(0) + str(0))
            number_1 = int(str(i)[1] + str(0))
            number_2 = int(str(i)[2])

            if (number_2 == 0 and number_1 == 0):
                letters_num = letters_num + len(numbers[number_0]) - 1 # -1 whitespace - hundrets
            elif number_2 == 0:
                letters_num = letters_num + len(numbers[number_0]) + len(numbers[number_1]) + len_and - 1
            elif number_1 == 0:
                letters_num = letters_num + len(numbers[number_0]) + len(numbers[number_2]) + len_and - 1
            elif number_1 == 10:
                letters_num = letters_num + len(numbers[number_0]) + len(numbers[int(str(number_1)[0] + str(number_2))]) + len_and -1
            else:
                letters_num = letters_num + len(numbers[number_0]) + len(numbers[number_1]) + len(numbers[number_2]) + len_and -1

    return letters_num

answer = letters_total(start_num, final_num)
print(answer)