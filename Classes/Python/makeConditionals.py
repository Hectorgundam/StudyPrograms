# Create a program that prints a message asking the user for a number between 1 and 100:

print("Please enter a number between 1 and 100:")
userNumber = int(input())

# a) If the number is less than 1, you must print a message “Please enter a number greater than 0”.
if userNumber < 1: 
    print("Please enter a number greater than 0.")

# b) If the number is greater than 100, you must print a message “Please enter a number less than or equal to 100”.
elif userNumber > 100: 
    print("Please enter a number less than or equal to 100.")

# c) If the number is between 1 and 100, it should print a message “Very good! He<número> It is a great option.
else: 
    print("Very good! The number" ,  userNumber , "is a great option.")
