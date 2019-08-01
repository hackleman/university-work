"""
We can determine how "out of order" an array A is by counting the number
 of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] 
but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. 
Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array 
[2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). 
The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
"""

def mergesort(arr):

    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:int(len(arr)/2)]
        b = arr[int(len(arr)/2):]

        a, ai = mergesort(a)
        b, bi = mergesort(b)

        c = []
        i = 0
        j = 0
        swaps = ai + bi

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i = i + 1
            else:
                if i < len(a):
                    print(a[i], b[j], a, b, swaps, len(a)-i)
                    swaps += len(a) - i
                c.append(b[j])
                j = j + 1

        c += a[i:]
        c += b[j:]
    return c, swaps



arr1 = [2, 4, 1, 3, 5]
arr2 = [5, 4, 3, 2, 1] 
print(mergesort(arr2))
