def mergeSort(arr):
    
    if len(arr) == 1:
        return arr
    else:
        a = arr[:int(len(arr)/2)]
        b = arr[int(len(arr)/2):]
        a, ai = mergeSort(a)
        b, bi = mergeSort(b)

        c = []
        i = 0
        j = 0

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i = i + 1
            else:
                c.append(b[j])
                j = j + 1
                print(len(a) - i)
                inversions += (len(a) - i)
        c += a[i:]
        c += b[j:]

    return c

arr = [6, 5, 4, 3, 2, 1]

print(mergeSort(arr))
