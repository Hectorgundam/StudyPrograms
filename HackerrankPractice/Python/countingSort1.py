# Comparison sorting 
# Python program 

# Quicksort usually has a running time of n x log(n), but us there are algorithm that can sort even faster? 
# In general, this is not possible. 
# Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. 
# A comparison sort algorithm cannot beat n x log(n) (worst-case) running time, since n x log(n) represents the minimum
# number of comparisons needed to know where to place each element. 

# Alternative sorting
# Another sorting method, the counting sort, does not require comparison.
# Instead, you create an integer array whose index range covers the entire range of values in your array to sort. 
# Each time a value occurs in the original array, you increment the counter at that index. 
# At the end, run through your couting array, printing the value of each non-zero valued index that number of times. 

# Example 
# arr = [1,1,3,2,1]

# All of the values are in the range [0...3], so create an array of zeros, result = [0,0,0,0]. The results of each iteration follow: 

# i   arr[i]  result
# 0       1   [0,1,0,0]
# 1       1   [0,2,0,0]
# 2       3   [0,2,0,1]
# 3       2   [0,2,1,1]
# 4       1   [0,3,0,0]

# The frequency array is [0,3,1,1]
# These values can be used to created the sorted array as well sorted=[1,1,1,2,3]

# Note 
# For this exercise, always return a frequency array with 100 elements.
# The example above shows only the first 4 elements, the remainder being zeros. 

# Challenge 
# Given a list of integers, count and return the number of times each value appears as an array of integers

# Function description 
# Complete the countingSort function in the editor 
# countingSort has the following parameters
# arr[n] is an array of integers 

# Returns 
# int[100] a frequency array 

# Input format
# The first line contains an integer n, the number of items in arr
# Each of the next n lines contains an integer arr[i] where 0 <= i < n

# Constraints
# 100 <= n <= 10^6
# 0 <= arr[i] < 100

# Sample input 
# 100
# 63 25 73 1 98 73 56 84 86 57 16 83 8 25 81 56 9 53 98 67 99 12 83 89 80 91 39 86 76 85 74 39 25 90 59 10 94 32 44 3 89 30 27 
# 79 46 96 27 32 18 21 92 69 81 40 40 34 68 78 24 87 42 69 23 41 78 22 6 90 99 89 50 30 20 1 43 3 70 95 33 46 44 9 69 48 33 60 
# 65 16 82 67 61 32 21 79 75 75 13 87 70 33  

# Sample output 
# 0 2 0 2 0 0 1 0 1 2 1 0 1 1 0 0 2 0 1 0 1 2 1 1 1 3 0 2 0 0 2 0 3 3 1 0 0 0 0 2 2 1 1 1 2 0 2 0 1 0 1 0 0 1 0 0 2 1 0 1 1 1 0 
# 1 0 1 0 2 1 3 2 0 0 2 1 2 1 0 2 2 1 2 1 2 1 1 2 2 0 3 2 1 1 0 1 1 1 0 2 2 

# Explanation
# Each of the resulting values result[i] represents the number of times i appeared in arr

import math
import os
import random
import re
import sys

def countingSort(arr): 

    # Test print to make sure arr was received as a parameter and check its contents 
    # print(arr)

    # Creating an array the same size of the one being received as a parameter 
    # Initializing all of it's cells to zero for now 
    # Will store the count of each number from 0 to 99
    counter = [0] * 100

    # Need to cycle through the elements in the array 
    for num in arr: 

        # Increasing the value of the number in the counter array
        # Basically if the value of num is currently 5, then counter[5] will be increased
        counter[num] += 1

    # Test print to check the contents of counter after sorting
    #print(counter)

    # Return the contents of counter
    return counter



if __name__ == '__main__': 

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())
    n = 100

    # arr = list(map(int, input().rstrip().split()))
    arr = [63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 99, 12, 83, 89, 80, 91, 39, 86, 76, 85, 74, 
           39, 25, 90, 59, 10, 94, 32, 44, 3, 89, 30, 27, 79, 46, 96, 27, 32, 18, 21, 92, 69, 81, 40, 40, 34, 68, 78, 24, 87, 42, 69,
             23, 41, 78, 22, 6, 90, 99, 89, 50, 30, 20, 1, 43, 3, 70, 95, 33, 46, 44, 9, 69, 48, 33, 60, 65, 16, 82, 67, 61, 32, 21, 
             79, 75, 75, 13, 87, 70, 33]
    
    # Test print to check the contents of arr 
    # print(arr)

    result = countingSort(arr)

    print(result)

    # fptr.write(' '.join(map(str, result)))
    
    # fptr.write('\n')

    # fptr.close()



