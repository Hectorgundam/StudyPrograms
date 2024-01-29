# Fizzbuzz
# Python program
# Program that uses conditionals to alter the contents of a numbered list based on parameters given

# Requirements:
#   - print list of integers 1 through 105
#   - replace integer with string "fizz" when integer is divisible by 3
#   - replace integer with string "buzz" when integer is divisible by 5
#   - replace integer with string "fizzbuzz" when integer is divisible by 3 as well as 5


#   - ensure that the code could be easily updated in the case of additional 
# requirements
 
# Expected results:
# 1
# 2
# fizz
# 4
# buzz
# fizz
# 7
# 8
# fizz
# buzz
# 11
# fizz
# 13
# 14
# fizzbuzz

# Extra Credit Requirements:
#   - replace integer with string "foo" when integer is divisible by 7
#   - replace integer with string "fizzfoo" when integer is divisible by 3 and 7
#   - replace integer with string "buzzfoo" when integer is divisible by 5 and 7
#   - replace integer with string "fizzbuzzfoo" when integer is divisible by 3,5 and 7

# Create a list of integers from 1 to 105 

# Our range is from 1 to 105 (does not include 0), can be customized later
n = 105

# Creating a list of integers starting from 1 to n + 1 (n is our range and + 1 to allocate space)
myList = list(range(1, n + 1))

# Creating a copy of myList called tempList to test out replacing the values instead of printing 
tempList = myList

# Creating a copy of myList called tempList to test out replacing the values instead of printing 
thirdList = myList

# Test printing the contents of myList 
# print("The contents of myList are", myList)

# First requirement is to print a list of integers 1 through 105 
# print(myList)

# Test printing the secondary list for testing purposes 
# Will be using this one to test out the replacement section of the requirements
# print(tempList)

# Cycling through the elements of our list for comparisons and replacements 
# Starting with prints to test out, will change to actual replacements later 
# For each element in myList
for i in myList: 

    # If the element is divisible by 3 
    if i % 3 == 0: 

        # Test print
        # print("Entered divisible by 3 condition, number was", i)

        # If the element is divisible by both 3 and 5 
        if i % 5 == 0: 

            # Test print
            # print("Entered divisible by 3 AND 5 condition, number was", i)

            print("fizzbuzz")

        # Otherwise it's just divisible by 3 
        else: 

            # Test print
            # print("Entered divisible by 3 but NOT by 5 condition, number was", i)

            print("fizz")

    # If the element is divisible by 5
    elif i % 5 == 0: 

        # Test print
        # print("Entered divisible by 5 condition, number was", i)

        print("buzz")

    # Otherwise print the number itself
    else: 

        print(i)


    
print("The contents of tempList are")
print(tempList)

# Cycling through the elements in tempList using indexing
for i in range(len(tempList)): 

    # If the element is divisible by 3 
    if i % 3 == 0: 

        # Test print
        # print("Entered divisible by 3 condition, number was", i)

        # If the element is divisible by both 3 and 5 
        if i % 5 == 0: 

            # Test print
            # print("Entered divisible by 3 AND 5 condition, number was", i)

            # print("fizzbuzz")

            # Replacing the contents of tempList index i with fizzbuzz
            tempList[i - 1] = 'fizzbuzz'

        # Otherwise it's just divisible by 3 
        else: 

            # Test print
            # print("Entered divisible by 3 but NOT by 5 condition, number was", i)

            # print("fizz")

            # Replacing the contents of tempList index i with fizz
            tempList[i - 1] = 'fizz'

    # If the element is divisible by 5
    elif i % 5 == 0: 

        # Test print
        # print("Entered divisible by 5 condition, number was", i)

        # print("buzz")

        # Replacing the contents of tempList index i with buzz
        tempList[i - 1]= 'buzz'

    # Otherwise print the number itself
    # else: 

        # print(tempList[i - 1])


# Test printing the new contents of tempList 
print("The new contents of tempList are")
print(tempList)

print("Testing extra credit requirements")

# Extra Credit Requirements:
#   - replace integer with string "foo" when integer is divisible by 7
#   - replace integer with string "fizzfoo" when integer is divisible by 3 and 7
#   - replace integer with string "buzzfoo" when integer is divisible by 5 and 7
#   - replace integer with string "fizzbuzzfoo" when integer is divisible by 3,5 and 7

# int % 7 == 0 foo 
# int % 3 == 0 and int % 7 == 0 fizzfoo 
# int % 5 == 0 and int % 7 == 0 buzzfoo
# int % 3 == 0 and int % 5 == 0 and int % 7 == 0 fizzbuzzfoo

print("The contents of thirdList are")
print(thirdList)

# Cycling through the elements in tempList using indexing
for i in range(len(thirdList)): 

    # If the element is divisible by 3 
    if i % 3 == 0: 

        # Test print
        # print("Entered divisible by 3 condition, number was", i)

        # If the element is divisible by both 3 and 5 
        if i % 5 == 0: 

            # Test print
            # print("Entered divisible by 3 AND 5 condition, number was", i)

            # print("fizzbuzz")

            # Replacing the contents of tempList index i with fizzbuzz
            thirdList[i - 1] = 'fizzbuzz'

        # Otherwise it's just divisible by 3 
        else: 

            # Test print
            # print("Entered divisible by 3 but NOT by 5 condition, number was", i)

            # print("fizz")

            # Replacing the contents of tempList index i with fizz
            thirdList[i - 1] = 'fizz'

    # If the element is divisible by 5
    elif i % 5 == 0: 

        # Test print
        # print("Entered divisible by 5 condition, number was", i)

        # print("buzz")

        # Replacing the contents of tempList index i with buzz
        thirdList[i - 1]= 'buzz'

    # Otherwise print the number itself
    # else: 

        # print(tempList[i - 1])
    # If the element is divisible by 7   
    elif i % 7 == 0: 

        thirdList[i - 1] = 'foo'

# Test printing the new contents of tempList 
print("The new contents of thirdList are")
print(thirdList)