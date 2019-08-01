ar = [1, 3, 2, 6, 1, 2]
count = 0

for _i in range(5):
    for _j in range(_i+1, 6):
        print(_i, _j, ar[_i], ar[_j])
        if (ar[_i] + ar[_j]) % 3 == 0:
            count += 1

print(count)