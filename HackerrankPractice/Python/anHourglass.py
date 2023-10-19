# An Hourglass
# Python program

# Given a 6 x 6 Array, arr 

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0 

# An hourglass in A is subset of values with indices falling in this pattern in arr's graphical representation

# a b c 
#   d
# e f global

# There are 16 hourglass in arr 
# An hourglass sum is the sum of an hourglass' values. 
# Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum
# The array will always be 6 x 6

# Example 

# arr = 
# -9 -9 -9 1 1 1
# 0 -9 0 4 3 2
# -9 -9 -9 1 2 3 
# 0 0 8 6 6 0
# 0 0 0 -2 0 0 
# 0 0 1 2 4 0 

# The 16 hourglass sums are 

# -63, -34, -9, 12,
# -10, 0, 28, 23,
# -27, -11, -2, 10, 
# 9, 17, 25, 18

# The highest hourglass sum is 28 from the hourglass beginning at row 1, column 2

# 0 4 3
#   1
# 8 6 6

# Function description
# Complete the function hourglassSum in the editor 
# hourglassSum has the following parameters 
# int arr[6][6] is an array of integers 

# Returns
# int is the maximum hourglass sum 

# Input format 
# Each of the 6 lines of inputs arr[i] contains 6 space-separated integers arr[i][j]

# Constraints 
# -9 <= arr[i][j] <= 9 
# 0 <= i, j <= 5

# Output formatPrint the largest (maximum) hourglass sum found in arr 

# Sample input

# 1 1 1 0 0 0
# 0 1 0 0 0 0 
# 1 1 1 0 0 0 
# 0 0 2 4 4 0
# 0 0 0 2 0 0 
# 0 0 1 2 4 0

# Sample output 

# 19 

# Explanation
# arr contains the following hourglasses 

# 1 1 1    1 1 0    1 0 0    0 0 0
#   1        0        0        0  
# 1 1 1    1 1 0    1 0 0    0 0 0 

# 0 1 0    1 0 0    0 0 0    0 0 0 
#   1        1        0        0
# 0 0 2    0 2 4    2 4 4    4 4 0

# 1 1 1    1 1 0    1 0 0    0 0 0 
#   0        2        4        4
# 0 0 0    0 0 2    0 2 0    2 0 0

# 0 0 2    0 2 4    2 4 4    4 4 0 
#   0        0        2        0
# 0 0 1    0 1 2    1 2 4    2 4 0

# The hourglass with the maximum sum (19) is 

# 2 4 4
#   2
# 1 2 4

import math 
import os 
import random 
import re 
import sys 

def hourglassSum(arr): 

    # Test print the contents of arr 
    # print("The parameter arr entered as ", arr)

    # Need a variable that will hold the contents of the maximum sum between the hourglasses
    # This one will be returned from the function at the end 
    maxSum = 0

    # Test print the contents of maxSum
    # print("The contents of maxSum are ", maxSum)

    # Cycling through 0 to 3 inclusive 
    for i in range(4):

        # Cycling through 0 to 3 inclusive
        for j in range(4): 

            # The currentSum will hold the values of adding up all the contents of one hourglass 
            currentSum = (arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
        
            # Test print to check the contents of currentSum
            # print("The contents of currentSum are ", currentSum)

            maxSum = max(maxSum, currentSum)
        
            # Test print to check the contents of maxSum
            # print("The contents of maxSum are ", maxSum)

    # Returning the maxSum
    return maxSum



if __name__ == '__main__':

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0], 
        [0, 0, 1, 2, 4, 0]
        ]

    # for _ in range(6):
        # arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    # Test printing the contents of result
    print(str(result))

    # fptr.write(str(result) + '\n')

    # fptr.close()