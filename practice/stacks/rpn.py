def reversePN(exp):
    stack = []

    for i in exp:
        
        if i == '+':
            result = int(stack.pop()) + int(stack.pop())
            stack.append(result)
        elif i == '-':
            result = int(stack.pop()) - int(stack.pop())
            stack.append(result)
        elif i == '*':
            result = int(stack.pop()) * int(stack.pop())
            stack.append(result)
        elif i == '/':
            result = int(stack.pop()) / int(stack.pop())
            stack.append(result)
        else:
            stack.append(i)

    print(stack.pop())
    
first = [ "3",  "4", "+", "2", "*", "1", "+" ]
reversePN(first)