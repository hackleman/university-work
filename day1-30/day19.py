import random

def generatearr():

    N = 10
    K = 5

    each = []
    arr = []
    for j in range(N):
        each = []
        for i in range(K):
            each.append(round(random.random()*9)+1)

        arr.append(each)

    print(arr)
    return arr

housearr = generatearr()



def minCost(housearr):

    #mincost of 10 houses is mincost of 9 houses plus min 
    #of current row that is not equal to end
    for i in range(1, len(housearr)):
        for j in range(len(housearr[0])):
            prev = housearr[i-1][:j] + housearr[i-1][j+1:]
            housearr[i][j] += min(prev)

    return housearr
"""
go through array grabbing min from each column
if each column happens to be non adjacent then the minimum is found
for the base case

now when we encounter a min value at the same index as the previous


"""
print(minCost(housearr))
