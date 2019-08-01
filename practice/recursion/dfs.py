A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
def flipAndInvertImage(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    length = int(len(A))
    print(length)
    for a in A:
        
        for i in range(int(length/2)):
            print(a, i, length-1)
            a[i], a[length-1-i] = 1 - a[length-1-i], 1-a[i]
            print(a)
        print(a)
        if length % 2 != 0:
            
            a[length/2] = 1 - a[length/2]

    return A

print(flipAndInvertImage(A))