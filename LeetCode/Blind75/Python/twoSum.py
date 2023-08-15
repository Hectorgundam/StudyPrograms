# Two Sum 

# Given an array of integers nums and an integer target, return indices of the two numbers such that they 
# add up to target. 
# You may assume that each input would have exactly one solution, and you may not sure the same element twice. 
# You can return the answer in any order. 
# Example
# Input - numbers = [2,7,11,15], target = 9
# Output - [0,1]
# Explanation - Because nums[0] + nums[1] == 9, we return [0,1]
# Constraints
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <=10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists. 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Dictionary to store the numbers and indexes
        indexCounter = {}

        # Cycling through the list while i is within the range of the length of the list
        for i, num in enumerate(nums):

            # Variable checker's value will be equal to the target value minus the          
            # value of num
            checker = target - num

            # If the current value of checker is within the dictionary indexCounter
            if checker in indexCounter:

                # We will return where that number was found and where checker is located
                return [indexCounter[checker], i]

            # Record the index where they were found
            indexCounter[num] = i

        # Otherwise, if we couldn't find the values that add up to the target value, we
        # return nothing
        return []

           
