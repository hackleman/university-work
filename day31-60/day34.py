def day34(string):

    def flip(string):
        a = list(string)
        b = ''
        for i in range(1, len(a)+1):
            b += a[-i]
        return b

    palindromes = []
    temp = ''

    # look for pivots
    for pos in range(1, len(string)):

        block = len(string[:pos])
        if flip(string[:pos]) == string[pos:pos+block]:
            temp = flip(string[pos:]) + string[pos:]
            palindromes.append(temp)

    # if not, pivots are start and end character
    temp = flip(string[1:]) + string[0] + string[1:]
    palindromes.append(temp)
    temp = string[:-1] + string[-1] + flip(string[:-1]) 
    palindromes.append(temp)

    print(palindromes)

string1 = 'google'
string2 = 'race'
day34(string2)

# print(flip('goo'))