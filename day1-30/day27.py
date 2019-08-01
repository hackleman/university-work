def checkCount(string, idx, brackets):

    if string[idx] == '(':
        brackets[0] += 1
    elif string[idx] == '{':
        brackets[1] += 1
    elif string[idx] == '[':
        brackets[2] += 1
    elif string[idx] == ')':
        brackets[0] -= 1
    elif string[idx] == '}':
        brackets[1] -= 1
    elif string[idx] == ']':
        brackets[2] -= 1



def checkCollision(string, idx):

    if idx + 1 < len(string):
        
        if string[idx] == '(' and string[idx + 1] == '}':
            print(string[idx], string[idx+1])
            return False
        elif string[idx] == '(' and string[idx + 1] == ']':
            print(string[idx], string[idx+1])
            return False        
        elif string[idx] == '{' and string[idx + 1] == ')':
            print(string[idx], string[idx+1])
            return False
        elif string[idx] == '{' and string[idx + 1] == ']':
            print(string[idx], string[idx+1])
            return False   
        elif string[idx] == '[' and string[idx + 1] == '}':
            print(string[idx], string[idx+1])
            return False
        elif string[idx] == '[' and string[idx + 1] == ')':
            print(string[idx], string[idx+1])
            return False   
        else:
            return True
    else:
        return True
        
string1 = '([])[]({})'
string2 = '([)]'
string3 = '((()'

brackets = [0] * 3

def driver(string, brackets):

    for i in range(len(string)):
        checkCount(string, i, brackets)
        if(not checkCollision(string, i)):
            return False
    
    if sum(brackets) != 0:
        return False
    
    return True

print(driver(string3, brackets))