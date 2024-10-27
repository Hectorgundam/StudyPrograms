# Find the Runner-Up Score 
# Python program

# Given the participant's score sheet for your University Sports Day, you are required to find the runner-up score. 
# You are given n scores. Store them in a list and find the score of the runner-up. 
# Input format 
# The first line contains n. 
# The second line contains an array A[] of n integers each separater by a space. 
# Constraints
# 2 <= n <= 10
# -100 <= A[i] <= 100
# Output format
# Print the runner-up score 
# Sample input 
# 5
# 2 3 6 6 5
# Sample output
# 5
# Explanation
# Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score. 

# In the initial problem the code showed as follows 
# n = int(input())
    
# arr = map(int, input().split())

# In order to get the code to work, I had to convert the map object into a list using list(mapObject)
# tempArr =  list(arr)

if __name__ == '__main__':

    # Asking the user for input 
    # n = int(input())

    # Test printing the contents of n 
    # print("The contents of n are", n)

    # arr = map(int, input().split())
    # Test case A 
    # n = 5
    # arr = [2, 3, 6, 6, 5]

    # Test case B
    # n = 4
    # arr = [57, 57, -57, 57]

    # Test case C 
    n = 5
    arr = [8, 7, 6, 5, 4]

    # Test case D 
    # n = 4
    # arr = [1, -1, -2, -1]

    # Test case E 
    # n = 5
    # arr = [6, 4, 5, 6, 6]

    # Test case F 
    # n = 10
    # arr = [6, 6, 6, 6, 6, 6, 6, 6, 6, 5]

    # Test printing the contents of arr 
    # print("The contents of arr are", arr)

    maxNum = max(arr)

    # Test printing the contents of maxNum
    # print("The contents of maxNum are", maxNum)

    runnerUp = None

    # Test printing the contents of runnerUp 
    # print("The contents of runnerUp are", runnerUp)

    # Cycling through the scores in our arr 
    for score in arr:

        # Test printing the current score 
        # print("The contents of score are", score)

        # If the score is equal to the maxNum then we pass up on it 
        # Since that would be the maximum, not the runner up 
        if score == maxNum: 

            # Test printing if we're passing 
            # print("Passing, the contents of score == maxNum")
            
            pass

        # If runnerUp is currently empty, lets give it the value of the current score  
        elif runnerUp == None: 

            # Test printing if runnerUp is being assigned its first value
            # print("Assigning first value to runnerUp, the contents of runnerUp were None")

            runnerUp = score

            # Test printing the contents of runnerUp
            # print("The contents of runnerUp are", runnerUp)

        # If the current score is higher than the runnerUp value then make the runnerUp value equal to the current score value     
        elif score > runnerUp: 

            # Test printing if score is greater than runnerUp 
            # print("The contents of score > runnerUp, changing contents of runnerUp")

            runnerUp = score

            # Test printing the contents of runnerUp 
            # print("The contents of runnerUp are", runnerUp)

    # Test printing the final value of runnerUp
    # print("The contents of runnerUp are", runnerUp)

    print(runnerUp)

        




    


