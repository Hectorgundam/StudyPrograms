# In progress

# Nested Lists 
# Python program 

# Given the names and grades for each student in a class of N students, store tem in a nested list and print the name(s)
# of any student(s) having the second lowest grade 

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name 
# on a new line 

# Example 
# records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]
# The ordered list of scores is [20.0, 50.0], so the second lowest score is 50.0
# There are two students with that score: ["beta", "alpha"] 
# Ordered alphabetically, the names are printed as: 
# alpha 
# beta 

# Input format 
# The first line contains an integer, N, the number of students 
# The 2N subsequent lines describe each student over 2 lines 
# - the first line contains a student's name 
# - the second line contains their grade 

# Constraints 
# 2 <= N <= 5 
# There will always be one or more students having the second lowest grade 

# Output format 
# Print the name(s) of any student(s) having the second lowest grade in 
# If there are multiple students, order their names alphabetically and print each one in a new line 

# Sample input A 
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina 
# 37.2
# Akriti
# 41
# Harsh
# 39 

# Sample output A 
# Berry 
# Harry 

# Explanation A 
# There are 5 students in this class whose names and grades are assembled to build the following list: 
# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# The lowest grade of 37.2 belongs to Tina
# The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print 
# each name on a new line 

if __name__ == '__main__': 

    # Creating a list that we can use to append/add the inputs we receive
    studentScores = []

    # Creating a list that we can use to store the scores 
    # Here we'll store the scores without duplicates, that way we can find the second lowest score 
    scores = []

    # For this exercise we go about it a bit differently since the platform is providing the input and we have to 
    # somehow read it and assign it 
    # Using a for loop to cycle through the inputs within the range given
    # for _ in range(int(input())): 

    #     # This is done by name = input() for the names and score = float(input()) 
    #     # In the case of score = float(input()) we can see that it's using the float() method to convert the input received 
    #     # into a float value 

    #     name = input()

    #     score = float(input())

    #     # Once a name and it's respective score have been obtained, we're adding/appending those to our nested list 
    #     studentScores.append([name, score])

    # # Test print 
    # print("The contents of studentScores are: ")
    # print(studentScores)

    # For the purpose of the program running outside of the platform environment, we'll use the equivalent / the result 
    # of the code above
    # studentScores will be our nested lists of student names with their respective scores 
    studentScores = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

    # Using this as a spacer to ease readability of our output for now
    print()

    # Test print 
    print("The contents of studentScores are: ")
    print(studentScores)

    # Using this as a spacer to ease readability of our output for now
    print()

    # The main factor I'm considering is the scores since we're trying to get the second lowest grade 
    # The problem is that we can't just sort the list of scores because there's a chance we might have duplicates and 
    # that gets in the way of getting the second lowest value 



