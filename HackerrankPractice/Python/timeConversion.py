# Time Conversion 
# Python program 

# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time 
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock 
# 12:00:00PM on a 24-hour clock is 12:00:00 on a 24-hour clock 

# Example 
# s = '12:01:00PM'
# Return '12:01:00'
# s = '12:01:00AM'
# Return '00:01:00'

# Function description 
# Complete the timeConversion function in the editor
# It should return a new string representing the input time in 24 hour format 
# timeConversion has the following parameters 
# string s is a time in 12 hour format 

# Returns
# strong for he time in 24 hour format 

# Input format 
# A single string s that represents a time in 12-hour clock format (i.e. hh:mm:ssAM or hh:mm:ssPM)

# Constraints
# All input times are valid

# Sample input 
# 07:05:45PM

# Sample output
# 19:05:45

import math 
import os
import random
import re
import sys

def timeConversion(s): 
    
    # String s is received as parameter with the time in hh:mm:ssAM or hh:mm:ssPM format 
    # Need to convert this to military time 

    # We know that 12:00:00AM is the equivalent of 00:00:00 in military time
    # From 12:00:00AM to 12:59:59PM the times match on both times 
    # After 12:59:59PM to 11:59:59PM we add 12 to every hour to get the equivalent in military time 
    # Then once we reach 12:00:00AM we reach the 24 hour mark, which resets to 00:00:00 in military time 

    # Checking if the string's last two elements are AM or PM 
    if s[-2:] == "AM":
        
        # Test print to make sure it entered the AM section 
        # print("it's AM")

        # If the first 2 elements of the string are 12 
        # Then we replace the first two elements with 00 and remove the AM section for our printing
        if s[:2] == "12": 
            # print("00" + s[2:-2])
            return "00" + s[2:-2]
        
        # If it's not 12 then we remove the AM section for our printing
        else:
            # print(s[:-2])
            return s[:-2]

    elif s[-2:] == "PM":

        # Test print to make sure it entered the PM section
        # print("it's PM")

        # If the first 2 elements of the string are 12 
        # Then we remove the PM section for our printing 
        if s[:2] == "12":
            # print(s[:-2])
            return s[:-2]

        # If it's not 12 then we take the integer value of the first two digits of our string and add 12 to them and remove the PM
        else: 
            # print(str(int(s[:2]) + 12) + s[2:-2])
            return str(int(s[:2]) + 12) + s[2:-2]


if __name__ == '__main__': 

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #s = input()

    #s = "11:59:59AM"

    s = "05:45:00PM"

    result = timeConversion(s)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
