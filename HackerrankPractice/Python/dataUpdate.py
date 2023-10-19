Incomplete
# Data updates 

# A data analyst recently joined as an intern 

# As an initial task, data for n days is provided to the intern 
# Then, k updates are performed on the data, where each update is of the form [l,r]
# This indicates that the subarray of data starting at index l and ending at index r is negated 
# For example, if data=[1,2,3,4] and the updates are [2,4] then the data becomes data = [1,-2,-3,-4]
# Given the initial data and k updates, find the final data after all updates 
# Note 1-based indexing is used 

# Example 
# Consider n=4, data=[1,-4,-5,2], k=2 and updates=[[2,4],[1,2]]
# After the first update, the data becomes data=[1,4,5,-2]
# After the second update, the data becomes data=[-1,-4,5,-2] 
# The final data is [-1,-4,5,-2]

# Function description 
# Complete the function getFinalData in the editor 

# getFinalData has the following parameters 
# int data[n] is the initial data
# int updates[k][2] is the updates in the form of [l,r]

# Returns
# int[n] the final data after all updates 

# Contraints 
# 1 <= n <= 10^5
# 1 <= k <= 10^5
# l data[i] l <= 10^9
# 1 <= updates[i][0] <= updates[i][1] <= n 

# Sample 1 input

# Pics

# Sample 1 output
# 3
# -1
# -3
# 0
# 7

# The updates are performed as follows 
# After the first update data=[-3,-1,-3,0,7]
# data=[-3,-1,3,0,-7]
# data=[3,1,-3,0,-7]
# data=[3,1,3,0,7]
# data=[3,-1,-,0,7]

# Python code 

#!/bin/python3

import math
import os
import random
import re
import sys




def getFinalData(data, updates):
    
    # We receive data and updates as parameters
    # Test print
    # print(data)
    
    # Test print
    # print(updates)
    
    # Need the length of the array
    n = len(data)
    
    # Testing 
    results = [0] * n
    
    # l and r are the indexes to be negated 
    for l, r in updates: 
        
        results[l-1] += 1 
        
        if r < n: 
            
            results[r] -= 1
        
    for i in range(1, n): 
        
        results[i] += results[i-1]
        
    for i in range(n): 
        
        results[i] = data[i] * (1 if results[i] % 2 == 0 else -1)
        
    # print(results) 
    
    return results
    
    
if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    data_count = int(input().strip())

    data = []

    for _ in range(data_count):

        data_item = int(input().strip())

        data.append(data_item)

    updates_rows = int(input().strip())

    updates_columns = int(input().strip())

    updates = []

    for _ in range(updates_rows):

        updates.append(list(map(int, input().rstrip().split())))

    result = getFinalData(data, updates)

    fptr.write('\n'.join(map(str, result)))
    
    fptr.write('\n')

    fptr.close()

