# Incomplete

# Grid Challenge 
# Python Program 

# Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending
# Determine if the columns are also in ascending alphabetical order, top to bottom
# Return YES of they are or NO if they are not 

# Example 
# grid = ['abc', 'ade', 'efg'] 

# The grid is illustrated below 
# a b c
# a d e 
# e f g 


# The rows are already in alphabetical order
# The columns a a e, b d f, and c e g are also in alphabetical order, so the answer would be YES
# Only elements within the same row can be rearranged 
# They cannot be moved to a different row 

# Function Description 
# Complete the gridChallenge function in the editor
# gridChallenge has the following parameters 
# string grid[n] is an array of strings 

# Returns
# string is either YES or None

# Input Format 
# The first line contains t, the number of testcases 
# Each of the next t sets of lines are described as follows 
# The first line contains n, the number of rows and columns in the grid 
# The next n lines contains a string of length n 

# Constraints 
# 1 <= t <= 100 
# 1 <= n <= 100
# Each string consists of lowercase letters in the range ascii[a-z]

# Output Format 
# For each test case, on a separate line print YES if it is possible to rearrange the grid alphabetically ascending 
# in both its rows and columns, or NO otherwise 

# Sample Input 
# STDIN   Function 
# 1       t = 1
# 5       n = 5
# ebacd   grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
# fghij
# olmkn
# trpqs
# xywuv

# Sample Output
# YES

# Explanation
# The 5x5 grid in the 1 test case can be reordered to 
# abcde 
# fghij 
# klmno 
# pqrst 
# uvwxy 

# This fulfills the condition since the rows 1, 2, ...,5 and the columns 1, 2, ..., 5 are all alphabetically sorted 

#!/bin/python3

import math
import os
import random
import re
import sys

def gridChallenge(grid):

    # Sort each row and create a new grid
    sorted_grid = [''.join(sorted(row)) for row in grid]

    # Check if columns are sorted
    # For each col in the range of the 
    for col in range(len(sorted_grid[0])):

        for row in range(1, len(sorted_grid)):

            if sorted_grid[row][col] < sorted_grid[row - 1][col]:

                return 'NO'

    return 'YES'

if __name__ == '__main__':

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input().strip())

    # for t_itr in range(t):

        # n = int(input().strip())

        # grid = []

        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']

        # for _ in range(n):
            
            # grid_item = input()
            
            # grid.append(grid_item)

        result = gridChallenge(grid)

        print(result)

        # fptr.write(result + '\n')

    # fptr.close()
