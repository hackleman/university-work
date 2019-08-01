"""
Given an integer k and a string s, 
find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

def driver(s, k, index, answers):

            # base case k=1, any string works
            # case k = 2, we can start at string of length 3
            if k==1 :
                return s[0]

        
def longestsubstring(s, k, i, answers) :

    if len(set(s[:i])) <= k and i > 0 :
        answers.append([s[:i], 0])
    elif i == 0:
       answers.append([s, 0])

    longestsubstring(s, k, i + 1, answers)


s = 'abcdcbacacabacbacbacb'
k = 3
index = 0

answers = []

s = [(ord(a)-96) for a in s]

#longestsubstring(s, k, index, answers)

for i in range(len(s)) :
   
    if len(set(s[:i+1])) <= k :
        answers.append([s[:i+1], 0])
        print(answers)

    # how are substrings related between n and n+1
    if len(set(s[:i+1])) > k :
        # we need longestsubstring(i-1) and its starting index
        
        print("index of: ", i)
        print('array is: ', s[:i+1])
        print('new value is: ', s[i])
        
        longest = answers[-1:][0][0]
        idx = answers[-1:][0][1]
        previous = longest
        print('longest answer (so far): ', longest)
        print('starting index is: ', idx)
        print('ending index is: ', len(longest) + idx - 1, "\n")
        # if the new character is contained in the longest string already and they are adjacent
        # append the new element to the answer 
        if (i == (len(longest) + idx)) and (s[i] in longest):

            
            longest.append(s[i])
        
            answers.append([longest, idx])
        temp = []
        tempidx = -1
        # if they are not adjacent, we have to determine if a string of adjacent characters starting from the right
        # is larger than the longest answer
        for j in range(len(s[:i+1])-1, -1, -1):

            temp.append(s[j])
            if len(set(temp)) > k :

                temp.pop()
                tempidx = j+1
                break

        if len(temp) > len(longest):
            temp.reverse()
            answers.append([temp, tempidx])
        #if set(answers[0]) == set(answers[0]+s[i]) :

        #longestsubstring(i-1)
        #indexoflongest(i-1)
answer = answers[-1][0]
final = [chr(a+96) for a in answer]
print(final, answers[-1][1])