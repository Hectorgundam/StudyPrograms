# Reverse a list 
# Python program 

# Given an array of integers, reverse the given array in place using an index and a loop rather than a built-in function 

# Example 
# arr = [1,3,2,4,5] 

# Return the array[5,4,2,3,1] which is the reverse of the input array 

# Function description
# Complete the function reverseArray in the editor 
# reverseArray has the following parameters 
# int arr[n] is an array of integers 

# Returns 
# int[n] the array in reverse order 

# Constrains 
# 1 <= n <= 100
# 0 < arr[i] <= 100

# Sample 1 input
# 5
# 1
# 3
# 2
# 4
# 5

# Sample output
# 5
# 4
# 2
# 3
# 1
# The input array is [1,3,2,4,5] so the reverse of the input array is [5,4,2,3,1] 

# Sample 2 input 
# 4
# 17 
# 10 
# 21 
# 45

# Sample output 
# 45
# 21
# 10
# 17

# The input array is [17,10,21,45] so the reverse of the input array is [45,21,10,17] 

# Python code 

#!/bin/python3

import math
import os
import random
import re
import sys

def reverseArray(arr):
    # Write your code here

    revArray = arr[::-1]

    for item in revArray:

        print(item)

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):

        arr_item = int(input().strip())

        arr.append(arr_item)

    result = reverseArray(arr)

    fptr.write('\n'.join(map(str, result)))

    fptr.write('\n')

    fptr.close()

