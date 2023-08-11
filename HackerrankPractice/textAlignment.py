# Text Alignment 

# In Python, a string of text can be aligned left, right and center. 

# .ljust(width)
# This method returns a left aligned string of length width. 
# >>> width = 20
# >>> print 'HackerRank'.ljust(width, '-')
# HackerRank----------

# .center(width)
# This method returns a centered string of length width.
# >>> width = 20
# >>> print 'HackerRank'.center(width, '-')
# -----HackerRank-----

# .rjust(width)
# This method returns a right aligned string of length width.
# >>> width = 20
# >>> print 'HackerRank'.rjust(width, '-')
# ----------HackerRank

# Task
# You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
# Your task is to replace the blank (______) with rjust, ljust or center.

# Input format
# A single line containing the thickness value for the logo. 
# Constraints
# The thickness must be an odd number. 
# 0 < thickness < 50
# Output Format 
# Output the desired logo. 

# Replace all _____ with rjust, ljust or center. 

# This must be an odd number
thickness = int(input())

c = 'H'

# Top cone
for i in range(thickness):
    print((c*i).______(thickness - 1) + c + ( c * i).______(thickness - 1))

# Top pillars
