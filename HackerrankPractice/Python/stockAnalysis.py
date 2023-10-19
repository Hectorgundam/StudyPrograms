# WIP - Incomplete

# An analyst is analyzing stock over a period of n days
# The price of the stock on the i^th day is price[i], and the profit obtained is denoted by profit[i]
# The analyst wants to pick a triplet of days (i, j, k) such that (i < j < k) and 
# price[i]<price[j] < price[k] in such a way that the total profit, ie profit[i] + profit[j] + profit[k] is maximized

# Find the maximum total profit possible
# If there is no valid tripled, return -1 

# Example 
# Consider n=5, price = [1,5,3,4,6], profit=[2,3,4,5,6] 

# An optimal triplet (considering 1-based indexing) is (3,4,5) 
# Here 3 < 4 < 6 and total profit = 4 + 5 + 6 = 15, the maximum possible
# So the answer is 15 

# Function description 
# Complete the function getMaximumProfit in the editor
# getMaximumProfit has the following parameter
# int price[n] that is the proces of the stock on each day 
# int profit[n] that is the profits obtained from the stock on each day 

# Returns
# long_int that is the maximum total profit 

# Constraints
# 1 <= n <= 4000
# 1 <= price[i], profit[i] <= 10^9 

# Sample case
# STDIN                           Function 
# 5                                price[] size, n=5
# 2                                price=[2,3,1,5,9] 
# 3
# 1
# 5
# 9
# 5                                 profit[] size, n=5 
# 1                                 profit=[1,2,6,1,5] 
# 2
# 6
# 1
# 5

# Sample output 
# 12

# Explanation
# An optimal triplet (considering 1-based indexing) is (3,4,5) 
# Here 1 < 5 < 9 and total profit=6+1+5=12 

# STDIN                           Function 
# 4                                price[] size, n=4
# 4                                price=[4,3,2,1] 
# 3
# 2
# 1
# 4                                 profit[] size, n=4
# 4                                 profit=[4,3,2,1] 
# 3
# 2
# 1


# Sample output 
# -1

# Explanation
# There is no valid triplet 



def getMaximumProfit(price, profit):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    price_count = int(input().strip())

    price = []

    for _ in range(price_count):
        price_item = int(input().strip())
        price.append(price_item)

    profit_count = int(input().strip())

    profit = []

    for _ in range(profit_count):
        profit_item = int(input().strip())
        profit.append(profit_item)

    result = getMaximumProfit(price, profit)

    fptr.write(str(result) + '\n')

    fptr.close()