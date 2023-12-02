Incomplete

# Palindrome Index 
# Python program 

# Given a string of lowercase letters in the range ascii[a-z], determine the index of a character that can be removed
# to make the string a palindrome. 

# There may be more than one solution, but any will do 

# If the word is already a palindrome or there is no solution, return -1
# Otherwise, return the index of a character to remove 

# Example
# s = "bcbc"

# Either remove 'b' at index 0 or 'c' at index 3

# Function description
# Complete the palindromeIndex function in the editor
# palindromeIndex has the following parameters 
# string s that is a string to analyze 

# Returns
# int that is the index of the character to remove or -1

# Input format 
# The first line contains an integer q, the number of queries
# Each of the next 1 lines contains a query string s 

# Constraints
# 1 <= q <= 20 
# 1 <= length of s <= 10^5 + 5
# All charactesr are in the range ascii[a-z] 

# Sample input 

# STDIN       Function 
# 3           q = 3 
# aaab        s = 'aaab' (first query)
# baa         s = 'baa' (second query)
# aaa         s = 'aaa' (third query) 

# Sample output 
# 3
# 0
# -1

# Explanation 
# Query 1 "aab"
# Removing 'b' at index 3 results in a palindrome, so return 3
# Query 2 "baa"
# Removing 'b' at index 0 results in a palindrome, so return 0 
# Query 3 'aaa'
# The string is already a palindrome, so return -1
# Removing any one of the charactesr would results in a palindrome, but this test comes first 


import math
import os
import random
import re
import sys

def palindromeIndex(s):
    
    # A palindrome is a set of letters that form a word that reads the same backwards as forwards 

    # Test printing the contents of s 
    print("The contents of s are", s)

    # Getting the size of the string received 
    size = len(s)

    # Test printing the contents of size
    print("The contents of size are", size)

    # If the palindrome is just 1 letter or nothing we return -1 
    if size <= 1: 

        # Test printing if condition was met 
        print("The condition size <= 1 was met")

        return -1
    



    


if __name__ == '__main__':

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # q = int(input().strip())

    # for q_itr in range(q):

        # s = input()
    s = "aab"
        
        # result = palindromeIndex(s)
    result = palindromeIndex(s)

        # fptr.write(str(result) + '\n')

    # fptr.close()

