# Symmetric Difference 
# Python Program 

# The mathematical term symmetric difference (△ or ⊕) of two sets is the set of elements which are in either 
# of the two sets but on in both. 
# For example, for sets A={1,2,3} and B={2,3,4}, A △ B = {1,4}
# Symmetric difference is a binary operation, which means it operates on only two elements. So to evaluate an
# expression involving symmetric differences among three elements (A △ B △ C), you must complete one operation
# at a tim. Thus, for sets A and B above, and C={2,3}, A △ B △ C = (A △ B) △ C = {1,4} △ {2,3} = {1,2,3,4}

# Create a function that takes two or more arrays and returns an array of their symmetric difference 
# The returned array must contain only unique values (no duplicates) 

# Giving symmetric Difference a shot manually 
def symmetricDifference(firstSet, secondSet): 

    # Test printing arguments received 
    print("The contents of argument firstSet are received as: ", firstSet)
    print("The contents of argument secondSet are received as: ", secondSet)

    # Turning these into sets that I can use to determine the symmetric difference 
    setOne = set(firstSet)
    setTwo = set(secondSet)

    # Test printing new sets 
    print("The contents of setOne are: ", setOne)
    print("The contents of setTwo are: ", setTwo)

    # 7
    result = (setOne - setTwo) | (setTwo - setOne)

    # Test printing the contents of result 
    print("The contents of result are: ", result)

    # Returning the contents of result, where the symmetric difference is contained after calculations
    return result

# Found a method that can be used, testing here 
def symmDiff(firstSet, secondSet):

    # Test printing arguments received 
    print("The contents of argument firstSet are received as: ", firstSet)
    print("The contents of argument secondSet are received as: ", secondSet)

    # Turning these into sets that I can use to determine the symmetric difference 
    setOne = set(firstSet)
    setTwo = set(secondSet)

    # Test printing new sets 
    print("The contents of setOne are: ", setOne)
    print("The contents of setTwo are: ", setTwo)

    # Using the symmetric_difference() method to determine the difference 
    # Takes two parameters parameterOne.symmetric_differece(parameterTwo)
    resultFromMethod = setOne.symmetric_difference(setTwo)

    # Test printing the contents of resultFromMethod 
    print("The contents of resultFromMethod are: ", resultFromMethod)

    return resultFromMethod

if __name__ == '__main__':

    # Printing the value of count
    print("Hello, and welcome to Symmetric Difference!")

    # Test cases 
    # firstSet = [1,2,3]
    # secondSet = [5,2,1,4]

    result = symmetricDifference([1,2,3],[5,2,1,4])

    print("Manual Symmetric Difference results are: ", result)
    
    resultFromMethod = symmDiff([1,2,3], [5,2,1,4])

    print("Symmetric Difference results through method are: ", resultFromMethod)