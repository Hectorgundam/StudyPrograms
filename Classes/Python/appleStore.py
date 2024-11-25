# 1. Print a message, welcoming the user and asking for their name.
print("Welcome to the Apple Store")

# 2. Now the user must enter their name.
print("Please enter your first name:")
firstName = input()

print("Please enter your last name:")
lastName = input()

fullName = firstName + " " + lastName

# 3. Print message, greeting the user by name, and indicating that you currently have 20 apples available, 
# each for a price of 5 (can be peso, euro, dollar, etc.).
print("Hi" , fullName , "!")

apples = 20 

appleCost = 5 

print("We currently have" , apples , "apples available for purchase, each one costs" , appleCost , "dollars.")

# 4. Print a message, asking the user how many apples they want to buy.
print("How many apples would you like to buy?")

# 5. Now the user must enter how many apples they want.
appleRequest = int(input())

# 6. Print a message indicating how many apples the user bought, and what the total price was.
userBalance = appleCost * appleRequest

print("You purchased", appleRequest , "apples. Which totals to" , userBalance , "dollars.")

print("Thank you for your purchase!")

# 7. Finally, print a message indicating how many apples were available after the sale.
apples -= appleRequest

print("We now have" , apples , "remaining. ")