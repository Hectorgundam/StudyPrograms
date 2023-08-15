# Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters. 

# Example
# Input: s = "abcabcbb"
# Output = 3
# Explanation: The answer is "abc", with the length of 3. 

# Constraints
# 0 <= s.length <= 5 * 10^4
# s consider of English letters, digits, symbols and spaces. 

class Solution: 

    def lengthOfLongestSubstring(self, s: str) -> int: 

        # A dictionary to store the most recent index of each character 
        indexCounter = {}

        # It will store the longest the substring that doesn't have repeating characters is
        maxLength = 0

        # Reference counter for our substring
        starter = 0 

        # Cycle through each character in the main string 
        # Loop runs while the incrementing value of i is within the range of the length of our string s
        for i in range (len(s)):

            # If the current character we're looking at is already in our dictionary and the index for it is
            # after our current starter counter
            if s[i] in indexCounter and indexCounter[s[i]] >= starter:

                # Variable starter will be equal to the current location of i within the string + 1
                # As in we are moving the starter to the next position after the character showed up
                starter = indexCounter[s[i]] + 1

            # Updating the index of the current character inside our dictionary 
            indexCounter[s[i]] = i

            # Determining the current length of the substring without repeating characters so far 
            currentLength = i - starter + 1

            # Using max() to determine whichever value is larger between maxLength and currentLength is and that's
            # what's going to replace maxLength's current value
            maxLength = max(maxLength, currentLength)
        
        # Once we've checked, then we can return the value of variable maxLength
        return maxLength




    

if __name__ == '__main__':

    # Code testing 
    solutions = Solution()

    input_string = "abcabcbb"

    result = solutions.lengthOfLongestSubstring(input_string)

    print(result)
