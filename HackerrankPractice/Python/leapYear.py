# Write a function 
# Leap Year

# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day.
# It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. 
# A leap year contains a leap day. 

# In the Gregorian calendar, three conditions are used to identify leap years: 

# The year can be evenly divided by 4, is a leap year, unless:
#     The year can be evenly divided by 100, it is NOT a leap year, unless:
#         The year is also evenly divisible by 400. Then it is a leap year. 

# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, 
#     while 1800, 1900, 2100, 2200, 2300, and 2500 are NOT leap years

# Task
# Given a year, determine whether it is a leap year. 
# f it is a leap year, return the Boolean True, otherwise return False.
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. 
# It is only necessary to complete the is_leap function. 
# Input formatRead year, the year to test. 
# Constraints
# 1900 <= year <= 10^5
# Output format
# The function must return a Boolean value (True,False). Output is handled by the provided code stub. 

def is_leap(year):

    # Will contain whether or not it's a leap year
    leap = False
    
    #Write your logic here
    # Determining whether the year entered by the user is a leap year or not
    if year % 4 == 0:

        if year % 100 != 0:
            leap = True

        else:
            if year % 400 == 0:
                leap = True
                
            else:
                leap = False

    else: 
        # Not divisible evenly by 4, it is not a leap year
        leap = False

    # Returning the value of leap
    return leap

# Asking the user for input and assigning the integer value to the variable year
year = int(input())

# Printing the result after calling the function is_leap while passing the year as the argument 
print(is_leap(year))

