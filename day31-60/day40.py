"""
Given an array of integers where every 
integer occurs three times except for 
one integer, which only occurs once, 
find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6],
 return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""
# def day40(arr):

arr = [6, 4, 3, 3, 3, 6, 6]

ones = 0
mults = 0

for a in arr:
    mults = mults | (ones & a)
    ones = ones ^ a

    notboth = ~(ones & mults)

    ones &= notboth
    mults &= notboth

print(ones)