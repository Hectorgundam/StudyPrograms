# Leap Year Calculator 

# Description 
# Program that checks if the year the user provides is a leap year or not

# Asking the user to enter a number 
userNumber = int(input("Enter the year you would like to check in the following format YYYY: "))

# Determining whether the year entered by the user is a leap year or not
if userNumber % 4 == 0:
    print("The number is divisible by 4. there's a chance it MIGHT be a leap year")

    if userNumber % 100 != 0:
        print("This number is also divisible by 100. It's a leap year.")

    else:
        if userNumber % 400 == 0:
            print("This number is also divisible by 400. It's a leap year.")
            
        else:
            print("It's not a leap year.")

else: 
    # Not divisible evenly by 4, it is not a leap year
    print("Tough luck, this is not a leap year. It's not divisible evenly by 4")
    