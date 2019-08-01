def breakingRecords(n):
    divisorsum = 0
    for num in range(1, int(n/2)):
        print(num, n)
        if n % num == 0:
            print(num)
            divisorsum += n
    print(divisorsum)

breakingRecords(20)
