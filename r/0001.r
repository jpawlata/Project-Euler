# Author: Justyna Pawlata
# Project Euler (https://projecteuler.net/)


# Problem 1:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

multiples_3_5 <- function(limit){
  numbers <- 1:limit
  numbers <- numbers[numbers %% 3 == 0 | numbers %% 5 == 0]
  return(sum(numbers))
}

multiples_3_5(1000)