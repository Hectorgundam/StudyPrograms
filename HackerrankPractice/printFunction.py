# Print Function 
# The included code stub will read an integer, n, from STDIN. 
# Without using any string methods, try to print the following:
# 123 . . . n
# Note that "..." represents the consecutive values in between. 
# Example 
# n = 5
# Print the string 12345
# Input formatThe first line contains an integer n. 
# Constraints
# 1 <= n <== 150
# Output format
# Print the list of integers from 1 through n as a string, without spaces. 

if __name__ == '__main__': 

    # Asking the user for input
    n = int(input())

    for i in range(n + 1):

        if (i > 0):
            print(f"{i}", end='')

