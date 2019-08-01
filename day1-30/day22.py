"""
Given a dictionary of words and a string made up of those
words (no spaces), return the original sentence in a list. 
If there is more than one possible reconstruction, return 
any of them. If there is no possible reconstruction, then 
return null.

For example, given the set of words 'quick', 'brown', 'the', 
'fox', and the string "thequickbrownfox", you should return 
['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 
'beyond', and the string "bedbathandbeyond", return either 
['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

"""
def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

final = []

"""
for i in range(2, len(answer[0])+1):

    temp = combinations(answer[0], i)
    new = list(''.join(w) for w in temp)
    final.append(new)
"""

str = 'bedbathandbeyond'
strset = ['bed', 'bath', 'bedbath', 'beyond', 'and']

def possiblesentences(str, strset):

    ptr = 0

    result = []
    results = [result]

    for idx in range(len(str)+1):

        if str[ptr:idx] in strset:

            if len(results) == 1:

                result.append(str[ptr:idx])
                ptr = idx

            elif len(results) == 2:

                results[0].append(str[ptr:idx])
                results[1].append(str[ptr:idx])

    # check for compound word inclusion

    return results

def findoverlapping(answer):

    newanswer = []

    for i in range(2, len(answer[0])+1):
        # start with first element and group strings together
        start = 0
        end = start + i

        while end < len(answer[0]) + 1 :

            temp = answer[0][start:end]
            ans = ''.join(temp)

            if ans in strset:

                newanswer = answer[0][:start] + answer[0][end:]
                newanswer.insert(start, ans)
                answer.append(newanswer)

            start += 1
            end += 1


answer = possiblesentences(str, strset)
findoverlapping(answer)

print(answer)