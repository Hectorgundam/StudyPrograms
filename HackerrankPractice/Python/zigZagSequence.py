Incomplete

# Zig Zag Sequence 
# Python program 

# In this challenge, the task is to debug the existing code to successfully execute all provided test files 

# Given an array of n, distinct integers, transform the array into a zig zag sequence by permuting the array elements
# A sequence will be called a zig zag sequence if the first k elements in the sequence are in increasing order and 
# the last k elements are in decreasing order, where k = (n + 1) / 2 
# You need to find the lexicographically smallest zig zag sequence of the given array

# Example 
# a = [2,3,5,1,4]
# Now if we permute the array as [1,4,5,3,2], the result is a zig zag sequence

# Debug the given function findZigZagSequence to return the appropriate siz zag sequence for the given input array
    
# Note: You can modify at most three lines in the given code. You cannot add or remove lines of code. 

# Input format 
# The first line contains t the number of test cases 
# The first line of each test case contains an integer n, denoting the number of array elements 
# The next line of the test case contains n elements of array a 

# Constraints 
# 1 <= t <= 20
# 1 <= n <= 10000 (n is always odd)
# 1 <= avi <= 10^9 

# Output format
# For each test cases, print the elements of the transformed zigzag sequence in a single line 

def findZigZagSequence(a, n): 

    # Test printing to check that a was received as a parameter and view its current contents 
    print("a entered function and is ", a)

    # Test printing to check that n was received as a parameter and view its current contents 
    print("n entered function and is ", n)

    # Need to sort the elements in the array 
    # Using the method sort(values) to sort the array 
    a.sort()

    # Test printing array a after sorting 
    print("The contents of a after sorting are ", a) 

    # Variable mid will be equal to the contents of the cell after the current value of n divided by 2 
    mid = int((n+1) / 2) - 1

    # Test print to check the contents of mid 
    print("The content of mid is ", mid)

    # 
    a[mid], a[n-1] = a[n-1], a[mid]

    # Test print the contents of a[mid]
    print("The contents of a[mid] are", a[mid])

    # Test print the contents of a[n-1]
    print("The contents of a[n-1]", a[n-1])

    # Test print the contents of a[mid] after swapping
    print("The contents of a[mid] after swapping are ", a[mid])

    # Test print the contents a[n-1] after swapping
    print("The contents of a[n-1] after swapping are ", a[n-1])

    st = mid + 1

    # Test print the contents of st 
    print("The contents of st are ", st)

    ed = n - 2

    # Test print the contents of ed 
    print("The contents of ed are ", ed)

    
    while(st <= ed): 

        # Test printing the current value of a[st]
        print("The current value of a[st] is ", a[st])

        # Test printing the current value of a[ed]
        print("The current value of a[ed] is", a[ed])

        # Swapping values 
        a[st], a[ed] = a[ed], a[st]

        # Test printing the current valies of a[st] and a[ed] after swapping
        # Test printing the current value of a[st] after swapping
        print("The current value of a[st] is ", a[st])

        # Test printing the current value of a[ed] after swapping
        print("The current value of a[ed] is", a[ed])

        # Test printing the current value of st 
        print("The current value of st is", st)

        # Test printing the current value of ed
        print("The current value of ed is ", ed)

        # Incrementing the value of st by 1
        st = st + 1 

        # Incrementing the value of ed by 1
        ed = ed - 1 

        # Test printing the current value of st 
        print("The current value of st after increment is", st)

         # Test printing the current value of ed
        print("The current value of ed after incrementing is ", ed)


    for i in range(n): 

        # Test printing the current value of i
        print("The current value of i is ", i)

        # If the current value of i is equal to te location of n-1
        if i == n-1: 

            # Test printing the current value of n-1
            print("The current value of n-1 is ",n-1)

            # Print the value of the current location that i is indexing
            print(a[i])

            # Test printing notification that we're exiting this function
            print("Leaving the if i == n-1 conditional statement")

        else: 

            # Testing printing that we entered into the else conditional
            print('Entered the else conditional')

            print(a[i], end = ' ')

if __name__ == '__main__':

    # test_cases = int(input())

    # for cs in range(test_cases): 

    # n = int(input())
        n = 5

    # Test print to check the contents of n 
        # print("The value of n is ", n)

    # a = list(map(int, input().split()))
        a = [2,3,5,1,4]

    # Test print the contents of a 
        # print("The contents of a are ", a)

        # findZigZagSequence(a, n) 
        result = findZigZagSequence(a, n)

        # Test print to check the contents of result 
        # print("The contents of result are ", result)

