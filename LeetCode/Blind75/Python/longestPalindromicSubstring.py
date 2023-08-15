# Longest Palindromic Substring 

# Given a string s, return the longest palindromic substring in s.
# Example 1
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer. 
# Constraints
# , <= s.length <= 1000
# s consists of only digits and English letters. 

# Palindrome means that it reads the same frontwards and backwards

class Solution: 

    def longestPalindrome(self, s: str) -> str:

        # Variable counter will be equal to the length of our string to determine how many characters are in it 
        counter = len(s)

        # Reference counter we'll use to remember where specific characers are later on
        starter = 0

        # This will help us determine the maximum length of the palindrome in our string
        maxLength = 1

        # If our counter's value is less than or equal to 1 then it's a special case: nothing or a 1 char palindrome
        if counter <= 1:

            # Return the string
            return s
        
        # Creating a table where we'll store our palindrome 
        checker = [[False] * counter for _ in range(counter)]

        # Cycling through and marking single characters as palindromes / special
        for i in range(counter):

            checker[i][i] = True

        # Cycling through and marking palindromes of two characters
        for i in range(counter - 1):

            # If the current value of index i is the same as the following index value
            if s[i] == s[i + 1]:

                # We will mark this part as special    
                checker[i][i + 1] = True 

                # Starter will hold the value of i to remember where the special character was found
                starter = i

                # The maxLength of the palindrome is 2 at this point
                maxLength = 2

        # Cycling through and marking palindromes of three characters or more 
        for length in range(3, counter + 1):

            # Cycling through while the incrementing value of i is within the range of the 
            # counter's value - the value of length + 1
            for i in range(counter - length + 1):

                # Variable j's value will be equal to the value of i + the value of length - 1
                j = i + length - 1

                # If the value in checker's cell i+1 j-1 and the string location i is equal to the string location j 
                # Basically the parts inside have to be special and the values have to be the same
                if checker[i + 1][j - 1] and s[i] == s[j]: 

                    # We mark this part as special
                    checker[i][j] = True

                    # If the current value of length is greater than the current value of maxLength
                    if length > maxLength: 

                        # We set the value of starter to the location of the longer one     
                        starter = i

                        # Variable maxLength will now be equal to the value of length since it's longer
                        maxLength = length

        # Return the longer palindrome
        return s[starter: starter + maxLength]

# For testing it out 
if __name__ == '__main__':

    solutions = Solution()

    input_stringA = "babad"

    input_stringB = "cbbd"

    input_stringC = "a"

    input_stringD = "loi"


    print(solutions.longestPalindrome(input_stringA))

    print(solutions.longestPalindrome(input_stringB))

    print(solutions.longestPalindrome(input_stringC))

    print(solutions.longestPalindrome(input_stringD))

