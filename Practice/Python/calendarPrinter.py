# Calendar Printer program

#Description
# Python program that prints out the calendar for given month and year 

# Example - If a month is 7 (July) and year is 2021, the output should be that month and year fully

# Importing Python's calendar module so we can use its objects
import calendar

# Intro to calendar program 
print("Welcome to the calendar month selector")

# Creating a variable called year which will contain the year entered by the user 
# Variable year will be equal to the integer value the user enters
year = int(input("Please enter the month in YYYY format: "))

# Creating a variable called month which will contain the month entered by the user
# Variable month will be equal to the integer value the user enters
month = int(input("Please enter the month in MM format, from 1-12: "))

# Printing the selected calendar month and year 
# Uses Python's built-in calendar module and uses a calendar object to print the contents
print(calendar.month(year, month))