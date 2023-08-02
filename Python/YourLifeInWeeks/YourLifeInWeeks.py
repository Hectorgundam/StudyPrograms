# Your Life in Weeks 

# Description
# Program that jokingly calculates how many days you have left to live if your lifespan was 
# exactly up to 90 years old based off an  article from Tim Urban
# Going based off this premise: 365 days in a year, 52 weeks in a year, 12 months in a year

# Asking the user for their age and assigning the integer value to the variable userAge
userAge = int(input("What's your current age? "))

# Determining how many years the user has left to live using a 90 year lifespan as a baseline
timeLeft = 90 - userAge

# Determining how many days the user has left to live using 365 days a year as a baseline
daysLeft = timeLeft * 365

# Determining how many weeks the user has left to live using 52 weeks a year as a baseline
weeksLeft = timeLeft * 52

# 
monthsLeft = timeLeft * 12

# Printing out the results to the user in a morbid yet jokingly way
print(f"Morbidly, we can say that you have {timeLeft} years left to live.")

print(f"Breaking that down further for perspective, that would be like {monthsLeft} months, \
{weeksLeft} weeks, or {daysLeft} days.")

print("Have a great day and try not to dwell too much on that, we don't all make it that far :)!")

