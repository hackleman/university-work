def traverse(start, length, arr, result):

    temp = []

    if len(result) > length:
        return

    # find all possible ending locations from current
    for _i in range(len(arr)):
        if arr[_i][0] == start:
            temp.append((arr[_i][1], _i))

    # sort list of ending locations alphabetically
    temp.sort()

    # if final element append destination
    if len(result) >= length: 
        result.append(start)
    
    # if we have a match
    if len(temp) > 0:
        result.append(start)
        arr.pop(temp[0][1])
        traverse(temp[0][0], length, arr, result)

    return
    
def itinerary(arr, start):
    
    result = []
    length = len(arr)
    traverse(start, length, arr, result)

    if len(result) == 1: return None

    return result

arr = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
arr2 =  [('SFO', 'COM'), ('COM', 'YYZ')]
arr3 = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]

start = 'YUL'
start2 = 'COM'
start3 = 'A'

print(itinerary(arr2, start2))
