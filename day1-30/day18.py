"""
For example, given array = [10, 5, 2, 7, 8, 7] 
and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. 
You can modify the input array in-place and you do
 not need to store the results.
 You can simply print them out as you compute them.
 """

def problem18(k, arr):

    max = []
    maxvalue = 0
    prev = arr[:k]

    for j in prev:
        if j > maxvalue: maxvalue = j

    max.append(maxvalue)

    for i in range(1, len(arr)-k+1):

        temp = arr[i:i+k]

        print("previous arrray is, ", prev)
        print("current array is, ", temp)
        print("maxvalue is: ", maxvalue)
        # check if max value is first element of prev array
        if maxvalue == prev[0]:
            print("going in")
            maxvalue = 0
            for j in temp:
                if j > maxvalue: maxvalue = j
        # if maxvalue is somewhere in temp
        else:
            if temp[-1] > maxvalue:
                maxvalue = temp[-1]
        
        max.append(maxvalue)

        prev = temp

    print(max)
k = 3
arr = [10, 5, 2, 7, 8, 7]

problem18(k, arr)