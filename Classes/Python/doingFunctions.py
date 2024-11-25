# To start, define a new function that takes 3 parameters. 
# This function must use the first parameter to decide what operation to do (addition, subtraction, multiplication or division) 
# and apply it to the remaining 2 parameters.

# Example: result = yourfunction(“multiply”, 5, 4). 
# (The result should be equal to 20)

# Note: 
# Here I am considering that the function is called “yourfunction” . 
# In your exercise, put whatever name you like for your function.

# userRequest()
# Function provides the user the list operations they can choose from
# Takes user input and returns the operation requested by the user 

# Need to modify it so that it validates that the operation entered by the user is valid 

import sys 

def userRequest(): 

    # Ask user what operation they would like to complete 
    print("What math operation would you like to do?")
    print("Please type one of the following options:")
    print("Addition")
    print("Subtraction")
    print("Multiplication")
    print("Division")

    operation = input()

    if validateOperationRequest(operation): 
        return operation

    else:
         print("")
         print("Invalid input, try again.")
         print("")

         userRequest()


# validateOperationRequest(operation)
# Function validateOperationRequest checks if the user input matches the operation list
def validateOperationRequest(operation): 
    if operation == 'Addition' or operation == 'Subtraction' or operation == 'Multiplication' or operation == 'Division': 
        # print("TEST - Validation condition is True")
        return True
    else: 
        # print("TEST - Validation condition is False")
        return False
    
# askNumber()
# Function asks the user to enter a number 
# If the input entered by the user is valid, convert into an integer and return the number 
# If the input entered by the user is invalid, ask the user to enter a number again by calling the function inside of itself 
# The function uses the function validateNumber(number) to verify if the user input is a number 
def askNumber():

    while True:

        number = input().strip()

        if validateNumber(number): 

            number = int(number)
            return number 
        else: 
            print("")
            print("Invalid number input, please enter a valid number:")

    
# validateNumber(number) 
# Checks that the value entered by the user is valid 
# Valid input is a number: negative, positive, decimal 
# Invalid number is: Empty string (user just hit Enter), empty spaces (user just hit Spacebar and Enter), words or characters 
def validateNumber(number): 

    try: 

        # Checking if the value entered by the user is a number by trying to convert the current string number into a float value 
        # If it can be converted then we return True 
        float(number)
        return True
    
    # If the before fails and we get basically a ValueError, we return False instead 
    except ValueError: 
        return False


def mathOperationRequest(operation, num1, num2): 
    
    if operation == 'Addition': 
        return num1 + num2 
    
    elif operation == 'Subtraction':
        return num1 - num2 
    
    elif operation == 'Multiplication': 
        return num1 * num2 
    
    elif operation == 'Division': 

        if num1 % num2 != 0: 
            return float(num1 / num2)
        
        else: 
            return int(num1 / num2)
        

# The user can select what math operation they want to do 
# Variable operation is a string 
    # Addition 
    # Subtraction 
    # Multiplication 
    # Division 

# The user can enter two numbers to process in the operation they requested 
    # num1
    # num2 

# Need a way to handle when the user enters a decimal number 
# Need a way to handle when the user enters negative numbers 
# Need a way to handle when the user enters no numbers 

# The funcion mathOperationRequested(operation, num1, num2) 
# Takes 3 parameters, the operation requested, first number and second number 
# The funcion processes the numbers using the operation requested by the user 

 # Welcome the user 
print("")
print("Welcome to the mini calculator!")
print("")

# Used as the determining condition for rerunning the calculator based on user input
calculatorRun = 'Yes'

while calculatorRun == 'Yes': 

    # userRequest()
    # Function provides the user the list operations they can choose from
    # Takes user input and returns the operation requested by the user 
    operation = userRequest()

    # validateOperationRequest(operation)
    # Function validateOperationRequest checks if the user input matches the operation list
    # If it matches the options the program continues 
    # If it doesn't match it - TOUGH LUCK 

    print("")

    print("You've selected" , operation)

    print("")

    print("Please enter the first number to use in the operation:")
    num1 = askNumber()

    print("")

    print("Please enter the second number to use in the operation")
    num2 = askNumber()

    print("")

    # Need to make an adjustment for when the user selects division
    result = mathOperationRequest(operation, num1, num2)

    if result != None:
        print("The result of the operation is" , result)

        print("")

    
    print("Do you want to rerun the calculator?")
    print("Type Yes to restart calculator.")
    print("Type No no close calculator.")
    calculatorRun = input()
    print("")

print("Thank you for using the mini calculator!")
print("")
sys.exit()