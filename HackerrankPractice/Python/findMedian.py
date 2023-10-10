# Find Median

# The median of a list of numbers is essentially its middle element after sorting. 
# The same number of elements occur after it as before. 
# Given a list of numbers with an odd number of elements, find the median? 

# Example 
# arr = [5,3,1,2,3]
# The sorted array arr' = [1,2,3,4,5]
# The middle element and the median is 3 

# Function description
# Complete the findMedian function in the editor
# findMedian has the following parameters 
# int arr[n] is an unsorted array of integers

# Returns 
# int the median of the array 

# Input format 
# The first line contains the integer n, the size of arrthe second line contains n space-separated integers arr[i]
 
# Constraints 
# 1 <= n <= 1000001
# n is odd
# -10000 <= arr[i] <= 10000

# Sample input 
# 7
# 0 1 2 4 6 5 3 

# Sample output 
# 3

# Explanation
# The sorted arr = [0,1,2,3,4,5,6]
# It's middle element is at arr[3]=3 

def findMedian(arr):

    # Test print to make sure arr was received as a parameter and check its contents 
    print("arr is entering function is ", arr)

    
    # Need to sort the numbers
    # Using 
    arr.sort()

    # Test printing what the contents of the array are after sorting 
    print("arr after sorting is ", arr)

    # Need a variable to store what the half-size of the array is
    # This will act as the location of the median
    half = len(arr) // 2

    # Test printing to see what the current value of half is 
    print("current value of half is ", half)

    # Test printing to check if location arr[half] is our median
    print("arr[half], the median, is ", arr[half])

    # Return the median 
    return arr[half]

if __name__ == '__main__':
    
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    n = 3

    # arr = list(map(int, input().rstrip().split()))

    # arr = [0,1,2,4,6,5,3]

    arr = [0,1,2,9,6,5,8]

    result = findMedian(arr)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()