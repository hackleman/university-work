n = int(input())

places = 0
leftover = n
compr = ''
maxrun = 1
temprun = 1

while(n > 1):
    n  = n / 2
    places += 1

for place in range(places):
    # print(leftover, 2 ** (places - place - 1))
    if leftover >= 2 ** (places - place - 1):
        compr += '1'
        leftover -= 2 ** (places - place - 1)
    else:
        compr += '0'

for index in range(len(compr)-1):
    print(compr[index], compr[index+1], temprun, maxrun)
    if compr[index] == '1' and compr[index+1] == '1':
        temprun += 1
        if index+1 == len(compr)-1:
            if temprun > maxrun:
                maxrun = temprun
    elif compr[index] == '1' and (compr[index+1] == '0'):
        if temprun > maxrun:
            maxrun = temprun
        temprun = 1


print(compr, maxrun)
