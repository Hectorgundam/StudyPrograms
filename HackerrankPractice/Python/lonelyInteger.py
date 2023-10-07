# Lonely integer 

# Given an array of integers, where all elements but one occur twice, find the unique element.

# Example 
# a = [1,2,3,4,3,2,1]
# The unique element is 4 

# Function description 
# Complete the lonelyInteger function in the editor 
# lonelyInteger has the following parameters 
# int a[n] is an array of integers 

# Returns
# int of the element that occurs only once 

# Input format 
# The first line contains a single integer, n, the number of integers in the array

# The second line contains n space-separated integers that describe the values in a 

# Constraints 
# 1 <= n <= 100
# It is guaranteed that n is an odd number and that there is one unique element 
# 0 <= a[i] <= 100, where 0 <= i < n

def lonelyInteger(a): 

    # Test print to check that the array was received as a parameter and view its contents

    # Variable that will hold the element that doesn't repeat in the array
    lonely = 0

    # Function receives an array of integer where 1 element is not repeated 
    # Need to cycle through the elements comparing the elements to check if they show up 
    # Need a method that can help me count the amount of times an element repeats or doesn't repeat 
    # Using myArray.count(value) to count
    # If the value is greater than 1 then the value repeats in the array
    # If the value of count is equal to 1 then the value doesn't repeat in the array 
    # Need a variable to store which element doesn't repeat and later return it 
    # Need to return variable that contains the unique element 

    # Need to cycle through the elements comparing the elements to check if they show up 
    for element in a: 

        # Checking if the amount of times that the value contained in element repeats in the array is equal to 1 
        # If it's not equal to 1 then continue checking since it means that the value repeats 
        # If it's equal to 1 
        if a.count(element) == 1:

            # The value contained in element only appears once in the array 
            # We assign the value contained in element to the variable lonely
            lonely = element 

            # We exit out of the loop once the unique value is found 
            break

    # Test print to see what value lonely is currently holding 
    # print(lonely) 

    # Return the variable that is holding the unique value 
    return lonely

if __name__ == '__main__': 

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # a = list(map(int, input().rstrip().split()))
    a = [1,2,3,4,3,2,1]


    result = lonelyInteger(a)

    # Test print to check what the function is returning
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
