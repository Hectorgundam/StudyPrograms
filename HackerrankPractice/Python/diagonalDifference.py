# Diagonal difference 

# Given a square matrix, calculate the absolute difference between the sums of its diagonals 
# For example, the square matrix arr is shown below 

# 1 2 3
# 4 5 6
# 9 8 9 

# The left-to-right diagonal = 1 + 5 + 9 = 15
# The right-to-left diagonal = 3 + 5 + 9 = 17 
# their absolute difference is |15 - 17| = 2 

# Function description 
# Complete the diagonalDifference function in the editor 
# diagonalDifference takes the following parameter 
# int arr[n][m] is an array of integers 

# Returns 
# int the absolute diagonal difference 

# Input format 
# The first line contains a single integer, n, the number of rows and columns in the square matrix arr 
# Each of the next n lines describes a row, arr[i] and consists of n space-separated integers arr[i][j] 

# Constraints 
# -100 <= arr[i][j] <= 100

# Output format 
# Return the absolute difference between the sums of the matrix's two diagonals as a single integer 

# Sample input 
# 3
# 11 2 4
# 4 5 6
# 10 8 -12 

# Sample output 
# 15 

# Explanation 
# The primary diagonal is 
# 11
#     5
#        -12
# Sum across the primary diagonal 11 + 5 - 12 = 4

# The secondary diagonal is 
#      4
#    5
# 10

# Sum across the secondary diagonal 4 + 5 + 10 = 19
# Difference |4 - 19| = 15

# Note |x| is the absolute value of x 

import math 
import os 
import random
import re
import sys

def diagonalDifference(arr): 

    # Test print to check that the matrix is being received as a parameter and checking it contents 
    # print(arr)

    # Need a variables to store the sums of the diagonals 
    leftDiagonal = 0 

    rightDiagonal = 0 

    # Need a way to determine the size of the matrix being received 
    n = len(arr)

    # Need to cycle through the elements in the matrix so the diagonal sums can be obtained 
    for i in range(n): 

        # We get the left diagonal when the row index and column index are the same 
        leftDiagonal += arr[i][i] 

        # We get the right Diagonal when the column index is n - 1 - row index 
        rightDiagonal += arr[i][n - 1 - i]

    # Test print to check what the value of leftDiagonal is currently 
    # print("Left diagonal is", leftDiagonal)

    # Test print to check what the value of rightDiagonal is currently
    # print("Right diagonal is", rightDiagonal)

    # Need a way to obtain the absolute difference of the two sums 
    # Subtracting rightDiagonal from leftDiagonal
    # Using the method abs(values)

    # Test print to check what the absolute difference of the two sums is 
    # print("The absolute difference is", abs(leftDiagonal - rightDiagonal))
    
    # Obtaining the absolute difference 
    return(abs(leftDiagonal - rightDiagonal))
    

if __name__ == '__main__':

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())
    n = 1

    # arr = []
    arr = [[11, 2, 4],
           [4, 5, 6],
           [10, 8, -12]]

    for _ in range(n): 

        # arr.append(list(map(int, input().rstrip().split())))

        result = diagonalDifference(arr) 

        print(result)

        # fptr.write(str(result) + '\n')

        # fptr.close()
