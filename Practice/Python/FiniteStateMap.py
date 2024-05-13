# Assignment: Map - Aplicatin of Finite State Machine 

# Game that places the user in a starting point with the goal of the user being able to make their way to the target location 

# Possible movements the user came make as keyboard input: 
# n for north (n) 
# s for south (s) 
# e for east (e) 
# w for west (w) 

# It's not always possible to move in any of the directions, in some cases you're limited to the movement direction given by the diagram 

# The program will ask the user in which direction they would like to move 
# The program then asks the user where they would like to move next through inputs of n, s, e, w 
# If the user can move to the new location based off the map/diagram then the user moves from one location to another, the program tells the user the name of the currentLocation, the name of the new location and how many times they've moved to arrive at that new location 
# If the user cannot move to the new location based off the map/diagram then no movement happens and the program asks the user for a direction to move again
# Once the user arrives at the target location the program congratulates them and tells them how many moves it took them to get to the target location and if it's a new record 
# The program then asks the user if they would like to play again or not 

# The program has to have a function called introduction() that prints out the following 
# Discrete Mathematics II
# Map Traveller Game 
# Travel from one village to another using (n)orth, (s)outh, (e)ast, (w)est. 
# Reach the destination village and win the game. 

# The program has to have a function called nextLand(land, direction) that takes in two arguments 
# Variable land will be one of the locations and variable direction will be a direction as n, s, e, or w 
# If the user can move to the next location with the direction selected by the user the function will return a string with the name of the current location and the one that the user will be moved to. The message should look like: 
# Starting at currentLocation. Try to reach nextLocation 

# Example: Starting at Maz. Try to reach Fer. 

# The program will then enter a while loop in which the function nextLand() will be called to help the user move through the map 
# In each iteration of the loop it will check if the user can move to another location with the direction they selected 
# If the user can move in the direction they selected, the new currentLocation should be updated. The program should tell the user where they are currently located, where they are going and how many movements it's taken them to get to the new currentLocation 
# If the user can't move in the selected location based on the map layout then the program should ask the user where to move again 
# The condition to close out the while loop is when the user arrives at the targetLocation. At which point the loop stops, the program then congratulates the user for reaching the targetLocation, tells them how many moves it took them to get to the targetLocation and if it's a new record. The program then asks the user if they would like to play again or not.  

# Based on the instructions, the program will assume that all responses entered by the user are correct 
# Because of this, I haven't added a failsafe to check for input and the program will crash if incorrect input is given 

# Running into a possible issue, there's a situation where we might run into a dead end 
# The section where Lex, Hon, Maz and Toy is contained in a way that if the user exits it, they can't come back into it 
# So if their destination was inside that section, they have no way of heading back into it since Mer cannot go west and Mit cannot go west 
# Do we take this into consideration when coding the program and create some form of failsafe to help the user get out of that issue? 
# The assignment doesn't list requirements to address this so will leave this for later if I have extra time 


# Using a dictionary as our map 
# Each key in our dictionary is going to be the village name 
# Then each value is another dictionary that shows the possible movements we can make from it 
# Breakdown to make sure I've got them correctly 
# Che can only move west to Mer 
# Mer can move east to Che, north to Mit 
# Toy can move east to Mer, west to Maz, north to Hon 
# Maz can move east to Toy, north to Lex 
# Lex can move south to Maz, east to Hon, north to Lam 
# Hon can move south to Toy, west to Lex 
# Lam can only move east to Mit 
# Mit can  move south to Mer, east to Fer 
# Fer can only move west to Mit 
map = {
    "Lam": {"e": "Mit"},
    "Lex": {"s": "Maz", "e": "Hon", "n": "Lam"},
    "Maz": {"n": "Lex", "e": "Toy"},
    "Toy": {"w": "Maz", "n": "Hon", "e": "Mer"},
    "Hon": {"w": "Lex", "s": "Toy"},
    "Mer": {"e": "Che", "n": "Mit"},
    "Che": {"w": "Mer"},
    "Mit": {"s": "Mer", "e": "Fer"},
    "Fer": {"w": "Mit"}
}

# Defining the introduction function 
# Function that prints out the name of the program and the instructions to navigate through it 
def introduction():

    # Adding these ------ lines for aesthetic, it was getting hard to read what was happenning, hope this is ok
    print("-------------------------------------------------------------------------------")
    print("Discrete Mathematics II")
    print("Map Traveller Game")
    print("")
    print("Travel from one village to another using (n)orth, (s)outh, (e)ast, (w)est.")
    print("Reach the destination village and win the game.")
    print("-------------------------------------------------------------------------------")
    print("")

# Defining the nextLand function 
# Function that takes two arguments: land is the name of the land and direction is one of the directions (n,s,e,w)
# Function that will determine the next village based on the user's current location and the direction they chose 
def nextLand(land, direction):
    
    # We return the next village in the direction the user selected 
    # If the user can't move in the selected direction then an empty string is returned 
    return map[land].get(direction, "")

# Defining the mainGame function 
# Function that contains the logic side of the game 
def mainGame():

    # Function call for introduction()
    introduction()

    # Variable that will store the best score in the game so far
    # Was having trouble getting this to work and found online that setting it to infinity could solve the issue
    # and it did solve the issue. 
    # Need to figure out why it solved it later 
    bestScore = float('inf')  # Initialize best score with infinity

    # A while loop that will run until the player finds the target location and decides not to play again 
    while True:

        # Starting the number of moves as 0 
        moves = 0

        # print("-------------------------------------------------------------------------------")

        # TESTING START - starting location validation

        # Trying to validate user input to make sure it's one of the locations in our map 
        # Using a while loop that will run until we hit the break that tells us the selected location is in our map
        while True: 

            # Asking the player to input the starting location/village
            currentLand = input("Choose your starting location: ").capitalize()

            # If the currentLand (location entered by the user) is in our map then we break out of this loop
            if currentLand in map: 

                break

            # If the currentLand (location entered by the user) is not in our map, then we notify the user 
            # and tell them to try again 
            # At which point the loop will run again since it didn't hit the break 
            else: 

                print("Invalid starting location. Please select a valid location")

        # TESTING END - starting location validation

        # TESTING START - target location validation

        # Trying to validate user input to make sure it's one of the locations in our map 
        # Using a while loop that will run until we hit the break that tells us the selected location is in our map
        while True: 
            
            # Asking the player to input the target location/village
            targetLand = input("Choose your target location: ").capitalize()
            
            # If the targetLand (location entered by the user) is in our map then we break out of this loop
            if targetLand in map: 

                break

            # If the targetLand (location entered by the user) is not in our map, then we notify the user 
            # and tell them to try again 
            # At which point the loop will run again since it didn't hit the break 
            else:

                print("Invalid target location. Please enter a valid location.") 

        # TESTING END - target location validation

        print("-------------------------------------------------------------------------------")

        # Printing the current location and the location the user is trying to reach 
        # Following instruction format as "Starting at currentLocation. Try to reach nextLocation"
        print(f"Starting at {currentLand}. Try to reach {targetLand}.")
        
        # A while loop that runs while the current location is not equal to the target location 
        # Or basically it runs until the target location is reached 
        while currentLand != targetLand:

            print("-------------------------------------------------------------------------------")

            # Telling the user their current location and asking in what direction they would like to move
            print(f"You are currently in {currentLand}.")

            # TEST START - direction validation 

            # Trying to validate user input to make sure it's one of the valid locations n, s, e, w 
            # Using a while loop that will run until we hit the break that tells us the selected direction is valid
            while True: 


                # The direction the user chose will be stored in the variable direction 
                # I know the instructions stated to assume the input would always be correct but I kept messing it up when testing 
                # So I added the .lower() to stop myself from accidentally inputting capitalized letters by "forcing" them to be lowercase
                direction = input("Choose a direction (n, s, e, w): ").lower()

                # If the direction entered by the user is within the accepted values then we break out of the loop and continue 
                if direction in ['n' , 's' , 'e' , 'w']: 

                    break
                
                # Otherwise if the direction entered by the user is not within the accepted values then we notify them and 
                # prompt them to enter one of the accepted values 
                else: 

                    print("Invalid direction, please enter 'n', 's', 'e', 'w'. ")


            # TEST END - direction validation 

            # Calling the function nextLand where we check if the user moved or not 
            # The function returns the name of the next location if the user can move to it 
            # The function returns an empty string if the user cannot move to another location 
            nextLanding = nextLand(currentLand, direction)

            # If nextLanding contains a string with the new location 
            if nextLanding:

                # Variable currentLand will contain the string returned by nextLanding which is the new location 
                currentLand = nextLanding

                # We increase the move counter by one since the player was able to move 
                moves += 1

                # We notify the user 
                print(f"Moved to {currentLand}. Total moves: {moves}")

            # Otherwise if nextLanding is an empty string and we ask the user to enter a location again    
            else:

                # We notify the user that they can't move in the direction they selected and ask them to select a new direction
                print("You can't move in that direction, try again.")

                # NOTES 
                # I'm a little confused on this part on whether or not we should increase the move counter 
                # Technically the user did try to make a move and could count as an attempt 
                # But the user didn't actually move 
                # Will take it as no increase for now and hopefully it'll be ok 
                # Otherwise the approach would've been to include a moves += 1 in this section as well or 
                # make it so that it was outside the if-else "window"
        
        print("-------------------------------------------------------------------------------")

        # If the number of moves the user made during this run was less than the bestScore 
        # In this case less moves would be a better record 
        if moves < bestScore:

            # The bestScore will be updated to the value of moves since it's the new best record 
            bestScore = moves

            # We congratulate the user since they made it to the target location, how many moves it took them to get there
            # and let them know they beat the best record 
            print(f"Congratulations! You reached {targetLand} in {moves} moves, which is a new record!")

        # If the number of moves the user made during this run was higher than the bestScore 
        else:

            # We congratulate the user since they made it to the target location and let them know how many moves it took them to get there 
            print(f"Congratulations! You reached {targetLand} in {moves} moves!")

        print("-------------------------------------------------------------------------------")

        # We ask the user if they want to play again and store their answer in playAgain
        # I know the instructions stated to assume the input would always be correct but I kept messing it up when testing 
        # So I added the .lower() to stop myself from accidentally inputting capitalized letters by "forcing" them to be lowercase
        playAgain = input("Would you like to play again? (yes/no): ").lower()

        print("-------------------------------------------------------------------------------")
        
        # If the value is not yet then we break out of the while loop to exit the game 
        if playAgain != "yes":
            break

        # TEST END - play again validation 
# Main section boiler plate for our Python program in which the mainGame function will be called 
if __name__ == "__main__":

    mainGame()
