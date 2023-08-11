# Find a string

# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring
# occurs in the given string. String traversal will take place from left to right, not from right to left. 
# Note
# String letters are case-sensitive.
# Input format
# The first line of input contains the original string.
# The next line contains the substring. 
# Constraints
# 1 <= lem(string) <= 200
# Each character in the string is an ascii character. 
# Output format
# Output the integer number indicating the total number of occurrences of the substring in the original string.
# Sample input
# ABCDCDC
# CDC 
# Sample output
# 2 
# Concept 
# Some string processing examples, such as these, might be useful. 
# There are a couple of new concepts: 
# In Python, the length of a string is found by the function len(s), where s is the string.
# To traverse through the length of a string, use a for loop:
# for i in range(0, len(s)):
#     print(s[i])
# A range function is used to loop over some length:
# range (0, 5)
# Here, the range loops over 0 to 4.5 is excluded. 

def count_substring(string, sub_string):

    # Counter variable 
    counter = 0 
    starter = 0

    # While the starter counter is less than the length of the main string
    while starter < len(string):

        # Finding the position where the sub_string is within the main string
        position = string.find(sub_string, starter)

        # If the sub_string isn't found in it then it returns -1
        if position == -1: 
            break

        # Increase the counter to keep cycling through
        counter += 1

        # Increase the starter counter by the current occurrence 
        starter = position + 1

    # Returning the value of count
    return counter

if __name__ == '__main__':

    # Asking the user for a string as input and 
    string = input().strip()

    # Asking the user for a sub_string as input and 
    sub_string = input().strip()

    # Variabe count will be equal to the value received after calling count_substring(string, sub_string)
    count = count_substring(string, sub_string)

    # Printing the value of count
    print(count)
