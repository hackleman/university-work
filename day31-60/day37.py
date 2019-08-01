def addsubset(arr, temp, n, t, idx):
    global results
    # t = index of temp
    # idx = index of arr
    # n = size of our subset
    if t == n :
        results.append(temp[:])
        temp = list(range(3))
        return
    
    if idx >= len(arr):
        return

    temp[t] = arr[idx]
    addsubset(arr, temp, n, t + 1, idx + 1)
    addsubset(arr, temp, n, t, idx + 1)


def powerset(arr):
    # find all subsets of length n
    for n in range(1, len(arr)):
        temp = list(range(n))
        addsubset(arr, temp, n, 0, 0)


arr = [1, 2, 3, 4, 5]
results = []
temp = []

results.append([])
powerset(arr)
results.append(arr)

print(results)