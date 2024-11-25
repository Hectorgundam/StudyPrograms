import random

# Function that "throws a dice) and returns the number for the user to guess 
# Function basically returns a random number between 2 and 12 using the random library 
def throwDice(): 
    return random.randint(2, 12)

def askPrediction(): 
    
    print("What number do you think it is?")
    prediction = int(input())

    return prediction


def printResult(number, userPrediction): 
    pass

10
while True: 

    number = throwDice()

    print("The number is" , number)

    userPrediction = askPrediction()

    if userPrediction == number: 
        break

    printResult(number, userPrediction)

    
print("You guessed the correct number, congratz! ")