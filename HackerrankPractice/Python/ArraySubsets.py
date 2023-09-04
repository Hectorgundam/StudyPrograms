# Given an integer array, divide the array into 2 subsets A and B while respecting the following conditions: 
#     - The intersection of A and B is null
#     - The union A and B is equal to the original array
#     - The number of elements in subset A is minimal
#     - The sum of A's elements is greater than the sum of B's elements 
# Return the subset A in increasing order where the sum of A's elements is greater than the sum of B's elements. If 
# more than one subset exists, return the one with the maximal sum. 
# Example
# n = 5
# arr = [3,7,5,6,2]
# The 2 subsets in arr that satisfy the conditions for A are [5,7] and [6,7]
#     - A is minimal (size 2)
#     - Sum(A) = (5+7) = 12 > Sum(B) = (2+3+6) = 11
#     - Sum(A) = (6+7) = 13 > Sum(B) = (2+3+5) = 10
#     - The intersection of A and B is null and their union is equal to arr
#     - The subset A where the sum of its elements is maximal is [6,7]
# Function Description
# Complete the subseA function in the editor below
# subsetA has the following parameters:
#     int arr[]: an integer array 
# Returns:
#     int[]: an integer array with the values of subset A
# Constraints
# 1<=n<=10^5
# 1<=arr[i]<=10^5 (where 0<=i<n)

def subsetA(arr):
    # Write your code here
    
    # Need to sort the array
    arr.sort()
    
    totalSum = sum(arr)
    sumB = 0 
    subA = []
    
    for num in reversed(arr):
        
        if totalSum - sumB > sumB:
            subA.append(num)
            sumB += num
        else: 
            break
        
    subA.sort()
    
    return subA
    

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = subsetA(arr)

    fptr.write('\n'.join(map(str, result)))

    fptr.write('/n')

    fptr.close()
