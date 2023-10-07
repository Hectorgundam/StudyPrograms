# Plus Minus

# Python program
# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
# Print the decimal value of each fraction on a new line with 6 places after the decimal. 
# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers
# with absolute error of up to 10^-4 are acceptable. 
# Example
# arr = [1,1,0,-1,-1]
# There are n=5 elements, two positive, 2 negative and one zero. Their ratios are 2/5 = 0.400000, 2/5=0.400000 and 1/5=0.200000. 
# Results are printed as 
# 0.400000
# 0.400000
# 0.200000

# Function description 
# Complete the plusMinus function in the editor. 
# plusMinus has the following parameter(s): 
# int arr[n] is an array of integer

# Print
# Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with 
# 6 digits after the decimal. The function should not return a value. 

# Input format
# The first line contains an integer, n, the size of the array 
# The second line contains n space-separated integers that describe arr[n] 

# Constraints
# 0 < n <= 100
# -100 <= arr[i] <= 100

# Output format
# Print the following 3 lines, each to 6 decimals 
# proportion of positive values
# proportion of negative values
# proportion of Zeros 

# Sample input
# STDIN               Function 
# 6                   arr[] size n = 6
# -4 3 -9 0 4 1       arr = [-4, 3, -9, 0, 4, 1]

# Sample Output 
# 0.500000
# 0.333333
# 0.166667

# Explanation
# There are 3 positive numbers, 2 negative numbers, and 1 zero in the array
# The proportions of occurrence are positive
# 3/6 = 0.500000, negative 2.6 = 0.333333 and zeros 1/6 = 0.166667


import math
import os
import random
import re
import sys

def plusMinus(arr):

    # Need a way to track of how many elements in total are in the array by using the length of the array received 
    counter = len(arr)

    # Need a way to keep track of how many instances of each integer type are in the array
    positives = 0
    negatives = 0
    zeros = 0 

    # We have to determine how many of each integer is contained within the array: positives, negatives, zeros
    # Using a loop to cycle through the array to find the elements of each type 
    for num in arr: 

        # Conditional statements will allow to increase the value of each variable for element type by 1 if it fits the criteria
        # If the current value of num is greater than 0, it's a positive and the value of positives is increased by 1 
        if num > 0: 
            positives += 1
        # If the current value of num is less than 0, it's a negative and the value of negatives is increased by 1
        elif num < 0: 
            negatives += 1
        # Otherwise the number is 0 and the value of zeros is increased by one
        else: 
            zeros += 1

    # Once we know the amount of each integer type we have then we determined the ratios: 
    # number of integer type / number of array elements
    # Print results onto the screen 
    # This function doesn't return anything so printing must happen from within it 
    # To format the result to decimal values with exactly 6 decimal places we use print("{:.6f}"".format(values))
    print("{:.6f}".format(positives / counter))

    print("{:.6f}".format(negatives / counter))

    print("{:.6f}".format(zeros / counter))


if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

