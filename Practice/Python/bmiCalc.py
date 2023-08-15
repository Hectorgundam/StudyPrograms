# BMI Calculator 
# Description:
# Python program that calculates body mass index (BMI) based on the user's input

# The formula to calculate body mass index is BMI = kg/m2 where kg 
# Where weight is in kilograms and m2 is height in meters squared (user enters cm)
# Assuming that height and weight entered will be positive integers
# Index being used for this particular program is: 
# Underweight = less than 18.5
# Normal = from 18.5 to 24.9 
# Overweight = from 25 to 29.9
# Obesity = 30 or greater

# Example - Height 150 Weight 52 BMI 23.1 Output Normal
# Example - Height 175 Weight 98 BMI 32 Output Obesity
# Example - Height 190 Weight 50 BMI 13.8 Output Underweight

# Intro message from the program to the user
print("Body Mass Index (BMI) Calculator")

# Asking user to enter their height in centimeters
height = float(input("Please enter your height in centimeters: ")) 

# User's height is being converted to meters squared
heightMeters = height / 100

# Asking user for their weight in kilograms
weight = float(input("Please enter your weight in kilograms: "))

# Calculating BMI and rounding the result to two decimals
BMI = round(weight / (heightMeters**2),1)

# Conditional statements to determine what category the user falls in based on BMI
if BMI < 18.5:
    category = "underweight"
elif BMI <= 24.9:
    category = "normal"
elif 25 <= BMI <= 29.9:
    category = "Overweight"
else:
    category = "Obesity"

# Printing the user's BMI
print(f"Your BMI is: {BMI}")

# Printing the category the user falls in based on BMI
print("Your results put you in the " + category + " category.")