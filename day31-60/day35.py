"""
Given an array of strictly the characters 
'R', 'G', and 'B', segregate the values of
 the array so that all the Rs come first, 
 the Gs come second, and the Bs come last. 
 You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], 
it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""

def rgb(arr):

    loc = 0

    for i in range(len(arr)):
        if arr[i] == 'R':

            arr[i], arr[loc] = arr[loc], arr[i]
            loc += 1


    for i in range(loc, len(arr)):
        if arr[i] == 'G':

            arr[i], arr[loc] = arr[loc], arr[i]
            loc += 1




array = ['G', 'B', 'R', 'R', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'B', 'R', 'G']
rgb(array)