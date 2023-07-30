# Python program
# Description
# Python program that calculates and prints the number of days between two given dates

# The user should be able to enter the two dates (one per line) with this format Year Month Day 
# The year must be formatted with for digits - Example 2021
# The month must be an integer between 1 and 12 (with no leading zeros) 
# The day must be an integer between 1 and 31 (with no leading zeros) 
# The first date must be previous or equal to the second date
# If the dates are equal (there are 0 days between them) display the message "The dates are equal"
# If there is only one day between the two dates, display the message "There is only 1 day between these dates."
# If the first date is later than the second date display the message "Please enter valid dates"

import datetime

# Ask the user for the first date
first_date = input("Enter the first date in YYYY/MM/DD format: ")

# Ask the user for the second date 
second_date = input("Enter the second date in YYYY/MM/DD format: ")

# Test
print(first_date)

print(second_date)

first_date = first_date.split("/")

second_date = second_date.split("/")

# Test 
print(first_date)

print(second_date)

first_year = int(first_date[0])

first_month = int(first_date[1])

first_day = int(first_date[2])

# Test 
print(first_year)
print(first_month)
print(first_day)

first_date_obj = datetime.date(first_year, first_month, first_day)

second_year = int(second_date[0])

second_month = int(second_date[1])

second_day = int(second_date[2])

# Test
print(second_year)
print(second_month)
print(second_day)


# Check if the user's entries are valid
# If user entries aren't valid - display a message stating that there is an error in their entry 
# If user entries aren't valid - display message stating how many days are in between the two dates

