first = [3, 0, 1, 3, 0, 5]

def day30(input):
    leftwall = -1
    rightwall = -1
    total = 0

    if input[0] > input[1]:
        leftwall = 0

    for i in range(1, len(input)-1):

        if input[i] > input[i+1] and input[i] > input[i-1]:

            if(leftwall > -1): rightwall = i
            else: leftwall = i

            minpeak = min(input[leftwall], input[rightwall])

            for i in input[leftwall:rightwall]:
                if (i < minpeak):
                    total += (minpeak-i)

            leftwall = rightwall
            rightwall = -1
    
    if input[-1] > input[-2]:
        rightwall = len(input)-1

        minpeak = min(input[leftwall], input[rightwall])

        for i in input[leftwall:rightwall]:
            if (i < minpeak):
                total += (minpeak - i)

    return total

print(day30(first))