"""
Given a stream of elements too large to store in memory, 
pick a random element from the 
stream with uniform probability.
"""

import random

def reservoir_sample( iter ):
    
    for k, item in enumerate(iter, start=1):
        if random.random() < (1.0 / k) :
            result = item

    return result

def reservoir_sample_err( iter ):
    
    n = 1
    result = iter[0]

    for item in iter:
        
        n += 1
        s = int(random.random() * n)
        if s < 1:
            result = item

    return result

iter = [22, 13, 5, 4, 23, 18]
distribution = [0] * len(iter)

for i in range(100000):

    result = reservoir_sample(iter)

    if result==iter[0]:
        distribution[0] += 1
    elif result==iter[1]:
        distribution[1] += 1
    elif result==iter[2]:
        distribution[2] += 1
    elif result==iter[3]:
        distribution[3] += 1
    elif result==iter[4]:
        distribution[4] += 1
    elif result==iter[5]:
        distribution[5] += 1

print(f"{distribution} is great")