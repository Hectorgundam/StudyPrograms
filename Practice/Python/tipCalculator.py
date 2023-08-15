# Tip Calculator 

# Description 
# Python program that calculates the amount a user should tip for service based on 
# the percentage they choose

# Introduction
print("Lets check how much you should tip for service!")

# Asking the user for the bill total
billAmount = float(input("How much was your total bill? $"))

# Asking the user what percentage they would like to tip for the service
# The amount is being divided by 100 to convert the amount the user provides to percentage
percentage = float(input("What percentage would you like to tip? ")) / 100

# Just adding humor
print("Ok cool, give me a second to check for you.")

# Calculating the tip amount by multiplying billAmount by percentage
tipAmount = round(billAmount * percentage)

# Just adding humor again
print("Alright boss, here's the breakdown:")

# Providing information to user
print(f"Bill total: ${billAmount}")

print(f"Tip: {percentage * 100}%")

print(f"Tip amount: ${tipAmount}")

# Calculating the total amount after tip by adding billAmount and tipAmount
totalAmount = round(billAmount + tipAmount)

# Printing out the totalAmount to the user 
print(f"And that totals your order to ${totalAmount}")

