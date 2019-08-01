"""
Compute the running median of a sequence of numbers. 
That is, given a stream of numbers, print out the median 
of the list so far on each new element.

Recall that the median of an even-numbered list is the 
average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], 
your algorithm should print out:
"""
def medianstream(stream):

    def printmedian(arr):
        median = 0
        if len(arr) == 1:
            median = arr[0]
        if len(arr) % 2 == 0:
            median = (arr[int(len(arr)/2)] + arr[int(len(arr)/2) - 1])/2
        else:
            median = arr[int(len(arr)/2)]
        print(median)

    arr = []

    for val in stream:

        if len(arr) == 0:
            arr.append(val)
            printmedian(arr)
            continue
        
        # smallest?
        if val < arr[0]:
            arr = [val] + arr
            printmedian(arr)
            continue

        # largest?
        if val > arr[len(arr)-1]:
            arr = arr + [val]
            printmedian(arr)
            continue
            
        # in the middle?
        for idx in range(len(arr)-1):

            if val > arr[idx] and val <= arr[idx+1]:
                arr = arr[:idx+1] + [val] + arr[idx+1:]
                printmedian(arr)
                break
    
    
stream = [2, 1, 5, 7, 2, 0, 5]
medianstream(stream)