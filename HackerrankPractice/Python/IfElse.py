# If-Else

# Given an integer, n, perform the following conditional actions: 
# If n is odd, print Weird 
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird 
# If n is even and greater than 20, print Not Weird
# Input formatA single line containing a positive integer, n. 
# Constraints 
# 1 <= n <= 100
# Output Format 
# Print Weird if the number is weird. Otherwise, print Not Weird. 

import math
import os
import random
import re
import sys

if __name__ == '__main__':

    # Asking the user for input and separating it 
    n = int(input().strip())

# If it's an odd number then it's weird, doesn't matter the range of it
    if (n % 2 != 0):
        print("Weird")
    
    # If it's an even number
    else: 
        
        # If it's an even number between the inclusive range of 2 through 20
        if (n >= 2) and (n <= 20):
            
            if(n >= 2) and (n <= 5):
                print("Not Weird")
                
            elif(n >= 6) and (n <= 20):
                print("Weird")
            
        # If it's even and above the inclusive range of 2 through 20
        else: 
            print("Not Weird") 
    