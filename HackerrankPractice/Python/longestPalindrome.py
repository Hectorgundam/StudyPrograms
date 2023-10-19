# WIP - Incomplete

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)  # Count how many letters are in the input word
        
        # If the word has only 1 or 0 letters, it's already a special word (palindrome)
        if n <= 1:
            return s
        
        # Create a table to remember if parts of the word are special (palindromes)
        dp = [[False] * n for _ in range(n)]
        
        start = 0  # We'll remember where the special part starts
        max_length = 1  # We'll remember how long the longest special part is
        
        # Mark all single letters as special (palindromes)
        for i in range(n):
            dp[i][i] = True
        
        # Check for special parts that have 2 letters
        for i in range(n - 1):
            if s[i] == s[i + 1]:  # If the two letters are the same
                dp[i][i + 1] = True  # Mark them as a special part
                start = i  # Remember the start of this special part
                max_length = 2  # Remember the length of this special part
        
        # Check for special parts that have 3 or more letters
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Check if the part between the 'i' and 'j' indexes is special (palindrome)
                # To be special, the part inside must be special and the letters at the ends must be the same
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True  # Mark this part as special
                    if length > max_length:  # If it's longer than the longest one we found
                        start = i  # Remember the start of this longer special part
                        max_length = length  # Remember the length of this longer special part
        
        # Return the longest special part (palindrome) we found
        return s[start:start + max_length]

# Example usage
solution = Solution()
input_string = "babad"
print(solution.longestPalindrome(input_string))  # Output: "bab" or "aba"