# Find the Highest Altitude

# There's a biker going on a roadtrip. The roadtrip consists of n+1 points at different altitudes. The biker starts his trip on 
# point 0 with altitude equal to 0. 
# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and i+1 for all 
# (0 <= 1 < n). Return the highest altitude of a point. 

# Example
# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

# Example
# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0 
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0. 

# Constraints
# n == gain.length
# 1 <= n <= 100
# -100 <= gain[i] <= 100

class Solution: 
    
    def largestAltitude(self, gain: list[int]) -> int:

        # Defining our current altitude
        currentAltitude = 0 

        # Defining what will be our maximum altitude 
        maxAltitude = currentAltitude 

        # Iterating through each item in the array for gain value
        for g in gain: 

            # Updating the current altitude by increasing its current value with the value contained in g 
            currentAltitude += g

            # Updating the maximum altitude by assigning the value that is highest between maxAltitude and currentAltitude 
            maxAltitude = max(maxAltitude, currentAltitude) 

        # After we finish cycling through the array we return what was the maximum altitude 
        return maxAltitude

solution = Solution()

gain1 = [-5,1,5,0,-7]
gain2 = [-4,-3,-2,-1,4,3,2]

print(solution.largestAltitude(gain1))

print(solution.largestAltitude(gain2))
