# List Comprehensions

# Let's learn about lists comprehensions! You are given three integers x, y and z representing the dimensions of
# a cuboid along with an integer n. Print a list of all possible coordinates (i,j,k) on a 3D grid where the sum of 
# i+j+k is not equal to n. Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z. 
# Please use list comprehensions rather than multiple loops, as a learning excerscise. 
# Example
# x = 1
# y = 1
# z = 2
# n = 3
# All permutations of [i,j,k] are:
# [[0,0,0][0,0,1][0,0,2][0,1,0][0,1,1][0,1,2][1,0,0][1,0,1][1,0,2]]
# Print an array of the elements that do not sum to n = 3
# [[0,0,0][0,0,1][0,0,2][0,1,0][0,1,1][1,0,0][1,0,1][1,1,0][1,1,2]]
# Input format
# Format integers x, y z and n, each on a separate line. 
# Constraints
# Print the list in lexicographic increasing order. 
# Sample input
# 1
# 1
# 1
# 2
# Sample output
# [[0,0,0][0,0,1][0,1,0][1,0,0][1,1,1]]
# Explanation
# Each variable x, y and z will have values of 0 and 1. All permutations of lists in the form 
# [i,j,k] = [[0,0,0][0,0,1][0,1,0][0,1,1][1,0,0][1,0,1][1,1,0][1,1,1]]
# Remove all arrays that sum to n=2 to leave only valid permutations. 

if __name__ == '__main__':

    # Asking the user for input
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Creating a list comprehension to cycle through the different variations
    myList = [

        # Creating the list for each combination of the variables i, j and k 
        [i,j,k]

        # Here we are cycling through while the incrementing value of our variables i, j and k respectively is 
        # within the range of the values contained within the variables x, y and z respectively 
        # Basically counting from 0 up to whatever value x, y and z are holding respectively 
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range (z + 1)

        # If the value obtained after adding the values of i, j and k is not equal to n 
        # We will add that to our list 
        if i + j + k != n
    ]

    # Print out the resulting list
    print(myList)