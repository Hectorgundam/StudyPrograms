# Caesar Cipher 
# Python program 

# Julius Caesar protected his confidential information by encrypting it using a cipher 
# Caesar's cipher shifts each letter by a number of letters 
# If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet 
# In the case of a rotation by 3, w, x, y and z would map to z, a, b and c 

# Original alphabet 
# abcdefghijklmnopqrstuvwxyz

# Alphabet rotated by 3 
# defghijklmnopqrstuvwxyzabc

# Example
# s = There's-a-starman-waiting-in-the-sky
# k = 3

# The alphabet is rotated by 3, matching the mapping above 
# The encrypted string is 
# Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb

# Note that the cipher only encrypts letters; symbols such as -, remain unencrypted 

# Function description 
# Complete the caesarCipher function in the editor 
# caesarCipher has the following parameters 
# string s is the cleartext 
# int k is the alphabet rotation factor 

# Returns
# string of the encrypted string 

# Input format 
# The first line containts the integer, n, the length of the unencrypted string 
# The second line contains the unencrypted string, s 
# The line contains k, the number of letters to rotate the alphabet by 

# Constraints 
# 1<= n <= 100
# 0 <= k <= 100
# s is a valid ASCII string without any spaces 

# Sample input 
# 11
# middle-Outz
# 2 

# Sample output 
# okffng-Qwvb 

# Explanation 
# Original alphabet 
# abcdefghijklmnopqrstuvwxyz

# Alphabet rotated 
# cdefghijklmnopqrstuvwxyzab

# m -> o
# i -> k
# d -> f 
# d -> f 
# l -> n 
# e -> g 
# - -> - 
# O -> Q 
# u -> w 
# t -> v 
# z -> b 

import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    
    # Parameter s is the string received 
    # Parameter k is the alphabet rotation factor 

    # Test printing the contents of s 
    # print("The contents of s are", s)

    # Test printing the contents of k 
    # print("The contents of k are", k)

    # Will be used to store the encrypted message that will be returned 
    encryptedMessage = [] 

    # Will help handle cases where k is greater than 26 
    # This helps us make sure that we only go from 0 to 25 (within the alphabet)
    k = k % 26 

    # Cycling through the elements in the string 
    for char in s:

        # If the character we're checking is a letter
        # This helps us make sure that numbers and symbols are ignored 
        # Using isalpha() to check if the characters are alphabet letters (a-z), will return true if it is
        if char.isalpha(): 

            # Using ord() to return an integer representing a Unicode character 
            # Using isupper() to check if the character is capitalized 
            shift = ord('A') if char.isupper() else ord('a')

            # Test printing the contents of shift 
            # print("The contents of shift are", shift)

            # Using chr() method to convert an integer to its unicode character and return it 
            # Using ord() to return an integer representing a Unicode character 
            encryptedMessage.append(chr((ord(char) + k - shift) % 26 + shift))

        # Otherwise, it's not a letter so we append it to the encrypted message as is 
        else: 
            
            # Using append() to add an element to the end of the list 
            encryptedMessage.append(char)

    # Returning the now encrypted message 
    # Using ''.join() to take all of the items in our iterable and join them into one string, with each element separated 
    # by a space
    return ''.join(encryptedMessage)


if __name__ == '__main__':

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # s = input()
    s = "There's-a-starman-waiting-in-the-sky"

    print("The contents of s are", s)

    # k = int(input().strip())
    k = 3

    result = caesarCipher(s, k)

    print("The contents of the encrypted message are", result)

    # fptr.write(result + '\n')

    # fptr.close()
