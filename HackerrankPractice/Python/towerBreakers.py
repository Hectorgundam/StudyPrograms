# Tower Breakers 
# Python program 

# Two players are playing a game of Tower Breakers! 
# Player 1 always moves first, and both players always play optimally 

# The rules of the game are as follows 
# Initially there are n towers 
# Each tower is of height m 
# The players move in alternating turns
# In each turn, a player can choose a tower of height x and reduce its height to y, where 1 <= y < x and y evenly divides x 
# If the current player is unable to make a move, they lose the game 

# Given the values of n and m, determine which player will win 
# If the first player wins, return 1 
# Otherwise return 2 

# Example 
# n = 2 
# m = 6 

# There are two towers, each of 6 units tall 
# Player 1 has a choice of two moves
# remove 3 pieces from a tower to leave 3 as 6 modulo 3 = 0 
# remove 5 pieces to leave 1 
# Let player 1 remove 3. Now the towers are 3 and 6 units tall
# Player 2 matches the move. Now the towers are both 3 units tall
# Now Player 1 has only one move 
# Player 1 removes 2 pieces leaving 1. Towers are 1 and 2 units tall 
# Player 2 matches again. Towers are both 1 unit tall 
# Player 1 has no move and loses. Return 2 

# Function description 
# Complete the towerBreakers function in the editor 
# towerBreakers has the following parameters 
# int n is the number of towers 
# int m is the height of each tower 

# Returns 
# int is the winner of the game 

# Input format 
# The first line contains a single integer t, the number of test cases 
# Each of the next t lines describes a test case in the form of 2 space-separated integers, n and m 

# Constraints 
# 1 < t <= 100
# 1 <= n, m <= 10^6

# Sample input 
# STDIN       Function 
# 2           t = 2
# 2 2         n = 2, m = 2 
# 1 4         n = 1, m = 4 

# Sample output 
# 2
# 1

# Explanation 
# We'll refer to player 1 as P1 and player 2 as P2 
# In the first test case, P1 chooses on of the two towers and reduces it to 1 
# Then P2 reduces the remaining tower to a height of 1 
# As both towers now have height 1, P1 cannot make a move so P2 is the winner

# In the second test case, there is only one tower of height 4
# P1 can reduce it to a height of either 1 or 2
# P1 chooses 1 as both players always choose optimally 
# Because P2 has no possible move, P1 wins 

import math 
import os 
import random 
import re 
import sys

def towerBreakers(n, m): 

    # Parameter n is the number of towers 
    # Parameter m is the height of the towers

    # Test printing the contents of parameter n 
    # print("The contents of n are ", n)

    # Test printing the contents of paramenter m 
    # print("The contents of m are ", m)

    # If the height of each tower is 1 then Player 2 wins 
    if m == 1: 

        # Return 2 to express that Player 2 won
        return 2
    
    # If the number of towers are even then the Player 2 wins 
    # If the remainder of the modulo division of n divided by 2 is equal to 0 
    elif n % 2 == 0: 

        # Return 2 to express that Player 2 won 
        return 2 
    
    # If the number of towers is odd then the Player 1 wins 
    # Otherwise 
    else: 

        # Return 1 to express that the Player 1 won 
        return 1 

if __name__ == '__main__':
    
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input().strip())

    # for t_itr in range(t):

        # first_multiple_input = input().rstrip().split()

        # n = int(first_multiple_input[0])

        n = 2


        # m = int(first_multiple_input[1])

        m = 2
        
        result = towerBreakers(n, m)

        print("The winner is Player", result)

        n = 1

        m = 4

        result = towerBreakers(n, m)

        print("The winner is Player", result)

        # fptr.write(str(result) + '\n')

    # fptr.close()