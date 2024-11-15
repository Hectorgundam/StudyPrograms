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

# In the code provided we can see that they are taking input for the names of the students and the scores as 
# two separate lists 

    # name = input()

    # score = float(input())

   # In our case we will hard code those lists for ease of access 

    # Cycling through the values while they are within the specified range/number of students 
    
    # List of names 
    names = ["Harry", "Berry", "Tina", "Akriti", "Harsh"]

     # Testing printing the contents of name 
    print("The contents of name are: ", names)

    # List of scores 
    scores = [37.21, 37.21, 37.2, 41, 39]

    # Test printing the contents of score 
    print("The contents of score are: ", scores)

    # Will contain a record of the students names with their associated scores 
    # Now that we have the lists, we need a way to join or associate these with each other 
    # We will append the name and score to records
    records = list(zip(names, scores))

     # Test printing the contents of records 
    print("The contents of records are: ", records)

    # Sorting records by grade 
    sortedScores = sorted(set(scores))

    # Getting the second lowest grade 
    secondLowestGrade = sortedScores[1]

    # Getting the names of students with the second lowest grade 
    secondLowestGradeStudents = [name for name, score in records if score == secondLowestGrade]

    # Sorting the names alphabetically 
    secondLowestGradeStudents.sort() 

    # Printing the names of the students 
    for student in secondLowestGradeStudents: 

        print(student)