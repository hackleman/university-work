def stocks(arr):
    max = -float('inf')
    for i in range(1, len(arr)):
        for j in range(i+1, len(arr)+1):
            if arr[-i] - arr[-j] > max:
                max = arr[-i] - arr[-j]
    return max
arr = [9, 11, 8, 5, 7, 10]
print(stocks(arr))