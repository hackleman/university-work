"""
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], 
the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, 
since we would not take any elements.
"""
def day49(arr):

    currentsum = 0
    maxsum = 0

    for i in range(len(arr)):

        currentsum += arr[i]

        if currentsum < 0:
            currentsum = 0
        
        maxsum = max(maxsum, currentsum)

    return maxsum

array = [34, -50, 42, 14, -5, 86]
arr = [-5, -1, -8, -9]
print(day49(arr))
