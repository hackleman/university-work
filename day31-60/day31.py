def editdistance(str1, str2):

    edits = 0

    if len(str1) > len(str2):
        str1, str2 = str2, str1
    
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            continue
        edits += 1
    
    edits += len(str2) - len(str1)
    print(edits)

    


str1 = 'kitten'
str2 = 'sitting'

editdistance(str1, str2)