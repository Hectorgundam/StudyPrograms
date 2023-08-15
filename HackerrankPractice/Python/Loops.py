# Loops

# The provided code stub reads an integer, n, from STDIN. 
# For all non-negative integers i<n, print i^2
# Example
# n=3
# The list of non-negative integers that are less than n=3 is [0,1,2]. Print the square of each number on a separate line. 
# 0
# 1
# 4
# Input Format 
# The first and only line contains the integer, n. 
# Constraints 
# a <= n <= 20
# Output format
# Print n lines, one corresponding to each i. 



if __name__ == '__main__':

    # Asking the user for input
    n = int(input())

    # Loop that cycles while the value of i is still in the range of n 
    for i in range(n + 1):

        # If the value of i is not negative and is less than the value of n
        # Raise the value of i to the power of 2
       if(i >= 0) and (i < n):
           print(f"{i ** 2}")

    

