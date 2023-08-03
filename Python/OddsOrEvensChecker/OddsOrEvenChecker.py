# Odd or Even Checker 
# Description
# Program that checks if a number is odd or even


# Asking the user to enter a number 
userNumber = float(input("Enter a number to check if it's even or odd: "))

# Checking if the user number is divisible by 2 without any remainder
# If there is a remainder then the number is odd
if userNumber % 2 == 0: 
    print(f"Number {userNumber} is even.")
else:
    print(f"Tough luck buddy, the number {userNumber} is odd.")