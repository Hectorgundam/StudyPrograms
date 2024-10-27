# WIP

# Recursive Digit Sum 
# Python program 

# We define super digit of an integer x using the following rules: 
# Given an integer, we need to find the super digit of the integer 
# - If x has only 1 digit, then its super digit is x 
# - Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x 

# For example, the super digit of 9875 will be calculated as: 
# super_digit(9875)     9 + 8 + 7 + 5 = 29
# super_digit(29)       2 + 9 = 11
# super_digit(11)       1 + 1 = 2 
# super_digit(2)        2

# Example
# n = '9875' 
# k = 4 

# The number p is created by concatenating the string n k times so the initial p = 9875987598759875
# superDigit(p) = superDigit(9875987598759875)      9 + 8 + 7 + 5 + 9 + 8 + 7 + 5 + 9 + 8 + 7 + 5 + 9 + 8 + 7 + 5 = 116
# superDigit(p) = superDigit(116)                   1 + 1 + 6 = 8
# superDigit(p) = superDigit(8)

# All of the digits of p sum to 116. The digits of 116 sum to 8. 8 is only one digit, so it's the super digit. 

# Function Description 

# Complete the fuction superDigit in the editor below. It must return the calculated super digit as an integer. 

# superDigit has the following parameter(s) 
# string n that is a string representation of an integer 
# int k that is the times to concatenate n to make p 

# Returns 

# int that is the super digit of n, repeated k times 

# Input Format 

# The first line contains two space separated integers, n and k 

# Constraints 

# 1 <= n <= 10^100000
# 1 <= k <= 10^5

#!/bin/python3 

import math 
import os 
import random 
import re 
import sys 

# Complete the superDigit funcion below 
# The function is expected to return an INTEGER 
# The function accepts the following parameters 
# STRING n 
# INTEGER k 

# Function definition for superDigit 
# Calculates the super digit of the number formed by repeating "n" for "k" times 
def superDigit(n,k): 

    # Using a helper function to calculate the super digit of a number represented as a string 
    def getSuperDigit(x):

        # If the length of the string is 1 then it's already a super digit and we can return it 
        if len(x) == 1: 
        
            # Returning the super digit when it's a single digit 
            return int(x)
        # Otherwise, it's more than a single digit and we can continue 
        # We call the function recursively in this case 
        else: 

            # The nextDigitX wil be the sum of the digits 
            nextDigitX = sum(int(digit) for digit in x)

            # Calling the function recursively to continue 
            return getSuperDigit(str(nextDigitX))
        
    # The initialSum will be the sum of the digits in n     
    initialSum = sum(int(digit) for digit in n)

    # The totalSum will be the initialSum multiplied by the value of k (to account for repetition)
    totalSum = initialSum * k 

    # We return the super digit of the totalSum by calling the helper function 
    return getSuperDigit(str(totalSum))
    


if __name__ == '__main__': 

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()