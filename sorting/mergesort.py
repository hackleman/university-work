def mergeSort(arr):

    if len(arr) == 1:
        return arr
    else:
        a = arr[:int(len(arr)/2)]
        b = arr[int(len(arr)/2):]
        l = mergeSort(a)
        r = mergeSort(b)

        c = []
        i = 0
        j = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                c.append(l[i])
                i = i + 1
            else:
                c.append(r[j])
                j = j + 1
        c += l[i:]
        c += r[j:]

    return c

arr = [6, 5, 4, 3, 2, 1]

print(mergeSort(arr))
