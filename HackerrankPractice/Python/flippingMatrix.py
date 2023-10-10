# Flipping the Matrix 
# Python program 

# Sean invented a game involving a 2n x 2n matrix where each cell of the matrix contains an integer 
# He can reverse any of its rows or columns any number of times 
# The goal of the game is to maximize the sum of the elements in the n x n submatrix located in the 
# upper-left quadrant of the matrix
# Given the initial configurations for q matrices, help Sean reverse the rows and columns of each matrix
# in the best possible way so that the sum of the elements in the matrix's upper-left quadrant is maximal

# Example
# matrix = [[1,2], [3,4]]
# 1 2
# 3 4

# It is 2 x 2 and we want to maximize the top left quadrant, a 1 x 1 matrix. Reverse row 1
# 1 2
# 4 3

# And now reverse column 0 
# 4 2
# 1 3

# The maximal sum is 4 

# Function description
# Complete the flippingMatrix function in the editor 
# flippingMatrix has the following parameters 
# int matrix[2n][2n] is a 2-dimensional array of integers

# Returns
# int the maximum sum possible 

# Input format 
# The first line contains an integer q, the number of queries
# The next q sets of lines are in the following format 
# The first line of each query contains an integer n 
# Each of the next 2n lines contains 2n space-separated integers matrix[i][j] in row i of the matrix

# Constraints 
# 1 <= q <= 16
# 1 <= n <= 128
# 0 <= matrix[i][j] <= 4096, where 0 <= i,j < 2n

# Sample input 
# STDIN         Function 
# 1             q=1
# 2             n=2
#               matrix=[[112,42,83,119],[56,125,56,49],\
# 56 125 56 49    [15,78,101,43], [62,98,114,108]]
# 15 78 101 43
# 62 98 114 18

# Sample output 414

# Explanation
# Start out with the following 2n x 2n matrix
# matrix = [[112, 42, 83, 119],
#           [56, 125, 56, 49],
#           [15, 78, 101, 43],
#           [62, 98, 114, 108]]

# Perform the following operations to maximize the sum of the n x n submatrix in the upper-left quadrant
# Reverse column 2([83,56,101,114] -> [114,101,56,83]), resulting in the matrix
# matrix = [[112,42,114,119],
#           [56,125,56,49],
#           [15,78,56,43],
#           [62,98,83,108]]

# Reverse row 0([112,42,114,119] -> [119,114,42,112]), resulting in the matrix
# matrix = [[119,114,42,112],
#           [56,125,101,49],
#           [15,78,56,43],
#           [62,98,83,108]]

# The sum of values in the n x n submatrix in the upper-left quadrant is 119+114+56-125 = 414 


def flippingMatrix(matrix):

    # Need a variable to hold the value that is half of the length of the matrix
    # Using len(value) to get the total length of the matrix and then dividing that value by two
    n = len(matrix) // 2

    # Test print to make sure the matrix is being received as a parameter and check its contents 
    # print[matrix]

    # Need a variabe to store the sum of the max elements
    total = 0 

    # Need a variable to store the maxValue as we cycle through the elements 
    maxValue = 0

    # Need to cycle through the elements in the matrix
    for i in range(n):

        # Cycling through the elements in the matrix's first array
        for j in range(n): 

            # Need to look for the maximum Value 
            # Variable maxValue will hold the value that max() returns 
            # Using the method max(values) to find the item with the highest value 
            # Using max(samePosition, mirroredRowPosition, mirroredColumnPosition, mirroredRowAndColumnPosition)
            maxValue = max(

                # Comparing the values in the same positions
                matrix[i][j], 

                # Comparing the value with its mirrored row position
                matrix[2 * n - i - 1][j], 

                # Comparing the value with its mirrored column position
                matrix[i][2 * n - j - 1], 

                # Comparing the value with its mirrored row and column position
                matrix[2 * n - i - 1][2 * n - j - 1]   
                
            )

            # Test printing the current value of maxValue
            # print("maxValue is currently ", maxValue)

            # Variable total will have the current value of maxValue added to its current value 
            total += maxValue

            # Test printing the current value of total
            # print("total is currently ", total)
    
    # Test printing to check the current value of total before returning it
    # print("total before returning is ", total)

    # Return the total, aka maximum value 
    return total

if __name__ == '__main__':

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # q = int(input().strip())
    q = 1
    
    # for q_itr in range(q):

        # n = int(input().strip())
    n = 2
    
        # matrix = []
    matrix = [[112, 42, 83, 119],
                    [56, 125, 56, 49],
                    [15, 78, 101, 43],
                    [62, 98, 114, 108]]

        #for _ in range(2 * n):

            #matrix.append(list(map(int, input().rstrip().split())))

    result = flippingMatrix(matrix)

    # Test printing to check what the current value of result is 
    print(result)

        # fptr.write(str(result) + '\n')

    # fptr.close()