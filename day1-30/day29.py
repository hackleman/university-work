def day29(string):

    prev = string[0]
    count = 1
    answer = ''

    for i in string[1:]:
        
        if i == prev:
            prev = i
            count += 1
        else:
            answer = answer + str(count) + prev
            prev = i
            count = 1
    
    answer = answer + str(count) + prev
    print(answer)


string = 'AAAABBBCCDAA'
day29(string)