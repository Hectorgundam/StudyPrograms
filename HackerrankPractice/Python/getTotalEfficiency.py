# getTotalEfficiency
# A coding competition is being organized on the HackerRank platform. All participants need to be grouped into teams
# where each team has exactly two candidates and the sums of their skills must be equal for all teams. the efficiency 
# of a team is the product of the skills of its members, e.g. for a team with skills [2,3], the efficiency of the team
# is 2 * 3 = 6
# Find the sum of the efficiencies of the teams. If there is no way to create teams that satisfy the conditions, return -1. 
# Notes
# All participants must be assigned to a team
# The answer is always unique
# Example
# The skills of the candidates are skill = [1,2,3,2]. They can be paired as [[1,3][2,2]]. The sum of skills for each team 
# is the same, i.e. 4.
# The efficiency is computed as: 
# Efficiency of [1,3] = 1 * 3 = 3
# Efficiency of [2,2] = 2 * 2 = 4
# Return the sum of efficiencies, 3 + 4 = 7
# Function Description
# Complete the function getTotalEfficiency in the editor below
# getTotalEfficiency has the following parameter: 
# int skill[n]: the skills of each candidate
# Returns
# long_int: the sum of the efficiencies if it is possible to form the teams, or -1 otherwise
# Constraints
# 1 <= n <= 10^5
# 1 <= skill[i] <= 10^5
# n is even 
# It is guaranteed that the answer is unique

# Complete getTotalEfficiency function below

# The function is expected to return a LONG_INTEGER
# The function accepts INTEGER_ARRAY skill as parameter

def getTotalEfficiency(skill):
    # Write your code here
    skillFrequency = {}
    
    totalEfficiency = 0 
    
    for s in skill: 
        
        if s in skillFrequency:
            skillFrequency += 1
        else:
            skillFrequency[s] = 1
    
    totalSkill = sum(skill)
    target = totalSkill // 2
    
    for s in skillFrequency:
        
        if s * 2 == target: 
            totalEfficiency += (s * (s-1)) / 2 * skillFrequency[s]
        elif target - s in skillFrequency:
            totalEfficiency += s * (target - s) * skillFrequency[s] * skillFrequency[target - s]
            skillFrequency[target-s] = 0 
            
    if totalEfficiency == 0: 
        totalEfficiency = -1
        return totalEfficiency
    else:
        return totalEfficiency









if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    skill_count = int(input().strip())

    skill = []

    for _ in range(skill_count):

        skill_item = int(input().strip())
        skill.append(skill_item)

        result = getTotalEfficiency(skill)

        fptr.write(str(result) + '\n')

        fptr.close()