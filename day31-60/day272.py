def validsubstring(string, index):

    if index + 1 < len(string):
        if string[index] == '(' and string[index+1] == ')':         
            return True
        elif string[index] == '[' and string[index+1] == ']':
            return True
        elif string[index] == '{' and string[index+1] == '}':
            return True

def solution(string):

    newstring = string
    prevstring = string
    i = 0

    while(i < len(newstring)):
        if validsubstring(newstring, i):
            prevstring = newstring
            newstring = prevstring[:i] + prevstring[i+2:]
            print(prevstring, newstring, i)
            i = 0
        else: 
            i += 1

    if len(newstring) == 0:
        print('well-formed brackets')
    else:
        print('invalid bracket combination')


string = '([])[]({})'
string2 = '([)]'
string3 = '((()'

solution(string3)