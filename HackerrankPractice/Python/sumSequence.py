# Given three integers, i,j and k, a sequence sum to be the value of i+(i+1) + (i+2)+(i+3)+...+ j + (j-1)+(j-2)+(j-3)+k (increment from i until it equals j, then decrement from j until it equals k). 
# Given the values i, j and k, calculate the squence sum as described 

# Example 
# i=5
# j=9
# k=6

# Sum all the values from i to j and back to k 
# 5+6+7+8+9+8+7=56

# Function description 
# Complete the function getSequenceSum in the editor 
# getSequenceSum has the following parameters 
# int i, int j, int k that are three integers 

# Returns
# long that is the value of the sequence sum 

# Constraints 
# -10^8 <= i, j, k <= 10^8
# i, k <= k

# Sample Case 0 
# STDIN         FUNCTION
# 0                   i=0
# 5                   j=5
# -1                 k=-1
 
# Sample output 
# 24

# Explanation 
# i=0
# j=5
# k=-1
# 0+1+2+3+4+5+4+3+2+1+0+-1=24

# Sample Case 1
# STDIN         FUNCTION
# -5                   i=-5
# -1                  j=-1
# -3                 k=-3

# Sample Output 
# -20 

# Explanation 
# i=-5
# j=-1
# k=-3
# -5+-4+-3+-2+-1+-2+-3=-20

import math
import os
import random
import re
import sys

# getSequenceSum function that receives i, j and k as parameters 
def getSequenceSum(i, j, k):

# Test printing that we received the parameters i, j, k and their contents 
    # print("Received i and its contents are", i)
    # print("Received j and its contents are", j)
    # print("Received k and its contents are", k)
    
    # Need a variable that will be changing its value as it cycles through 
    # This variable needs to have the contents of i as a starting point 
    totalSum = 0
    
    # From i we count upwards until we reach j 
    # While our totalSum is less than j we increase the value of it 
    for num in range(i, j+1): 
        
        # The value of totalSum will be incremented by the value of num
        totalSum += num
        
        # Test printing current value of totalSum 
        # print(totalSum) 
        
    # From j we count downwards until we reach k 
    # While our totalSum is greater than k we decrease the value of it 
    for n in range(j-1, k-1, -1): 
        
        # The value of totalSum will be incremented by the value of n
        totalSum += n
        
        # Test printing current value of totalSum 
        # print(totalSum) 
    
    # Return the results
    return totalSum

if __name__ == '__main__':

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # i = int(input().strip())
    i = -5

    # j = int(input().strip())
    j = -1

    # k = int(input().strip())
    k = -3

    # Function call and assigning return value to res
    res = getSequenceSum(i, j, k)

    # Print out the current value of res
    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()