# Python program
# Description
# Program that calculates and prints the number of days between two given dates

# Importing the datetime module
import datetime

# Asking the user for the first date
first_date = input("Enter the first date in YYYY/MM/DD format: ")

# Asking the user for the second date 
second_date = input("Enter the second date in YYYY/MM/DD format: ")

# Splitting and assigning variable values for the first date
first_date = first_date.split("/")

first_year = int(first_date[0])

first_month = int(first_date[1])

first_day = int(first_date[2])

first_date_obj = datetime.date(first_year, first_month, first_day)

# Splitting and assigning variable values for the second date
second_date = second_date.split("/")

second_year = int(second_date[0])

second_month = int(second_date[1])

second_day = int(second_date[2])

second_date_obj = datetime.date(second_year, second_month, second_day)

# If the user's entry is not valid - tell the user that the dates entered aren't valid
if second_date_obj < first_date_obj:
    print("Please enter valid dates.")

else:
# The user's entry is valid so now we can check how many days are in between the dates entered

    days_in_between = (second_date_obj - first_date_obj).days

    if days_in_between == 0:
        print("You entered the same dates.")

    elif days_in_between == 1: 
        print("There's one day in between.")
    
    else:
        print(f"There are {days_in_between} days in between the two dates entered.")

