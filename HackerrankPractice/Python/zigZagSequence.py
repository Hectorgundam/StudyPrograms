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

    # Test printing the contents of a 
    print("The contents of a are ", a)

    # Test printing the contents of n 
    print("The contents of n are ", n) 

    # Sorting the contents of a 
    # Using .sort() to sort the contents in ascending order for now 
    a.sort()

    # Test printing the sorted contents of a 
    print("The contents of a after sorting are ", a)

    # Variable mid will be equal to the integer value of the contents of n + 1, divided by 2 and then subtracted 1 
    # This will give us the midline number 
    mid = int((n + 1)/2)-1

    # Test printing the contents of mid 
    print("The contents of mid are ", mid)

    # The contents of a[mid] and a[n-1] will be equal to the contents of a[n-1] and a[mid] respectively 
    a[mid], a[n-1] = a[n-1], a[mid]

    # Test printing the contents of a[mid] 
    print("The contents of a[mid] are ", a[mid])

    # Test printing the contents of a[n-1]
    print("The contents of a[n-1] are ", a[n-1])

    # The contents of st will be equal to the contents of mid after adding 1 to it
    st = mid + 1

    # Test printing the contents of st 
    print("The contents of st are ", st) 

    # The contents of ed will be equal to the contents of n after subtracting 2 to it 
    ed = n - 2

    # Test printing the contents of ed 
    print("The contents of ed are ", ed)

    # Cycling while the contents of st are less then or equal to the contents of ed 
    while(st <= ed):

        # Test printing if the contents of st are less than or equal to ed 
        print("The contents of st <= ed are ", (st<=ed))

        # The contents of a[st] and a[ed] will be equal to the contents of a[ed] and a[st] respectively 
        a[st], a[ed] = a[ed], a[st]

        # Test printing the contents of a[st]
        print("The contents of a[st] are ", a[st])

        # Test printing the contents of a[ed]
        print("The contents of a[ed] are ", a[ed])
    
        # The content of st will be equal to the current contents of st increased by 1 
        st = st + 1

        # Test printing the contents of st 
        print("The contents of st are ", st) 

        # The content of ed will be equal to the current contents of ed decreased by 1 
        ed = ed - 1

        # Test printing the contents of ed 
        print("The contents of ed are ", ed)

    # Cycling through the array elements while the value of i is within the range of the value of n 
    for i in range (n):

        # if the current value of i is equal to the current value of n decreased by 1 
        if i == n-1:

            # Test printing if i == n-1 
            print("The current contents of i == n-1 is ", (i==n-1))

            # We print the array cell of i index 
            print(a[i])

        # Otherwise
        else:

            # We print the array cell of i index with a space at the end 
            print(a[i], end = ' ')

    # We return nothing from the function since the printing was done from within it 
    return

if __name__ == '__main__':

    # test_cases = int(input())

    # for cs in range(test_cases): 

    # n = int(input())
        # n = 5
        n = 7

    # Test print to check the contents of n 
        # print("The value of n is ", n)

    # a = list(map(int, input().split()))
        # a = [2,3,5,1,4]
        a = [1,2,3,4,5,6,7]

    # Test print the contents of a 
        # print("The contents of a are ", a)

        # findZigZagSequence(a, n) 
        result = findZigZagSequence(a, n)

        # Test print to check the contents of result 
        # print("The contents of result are ", result)

