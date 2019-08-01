"""
Using a function rand5() that returns an integer from 1 to 5 (inclusive) 
with uniform probability, implement a function rand7() that returns an 
integer from 1 to 7 (inclusive).
"""
import random

# def rand2():

#     i = 5 * (random.randint(1, 5)-1) + random.randint(1, 5)
#     if i == 4: return rand2()
#     else: return i % 2

# def rand7():
#     i = rand2() * 4 + rand2() * 2 + rand2()
#     if (i == 7): return rand7()
#     else: return i
def rand5():
    return random.randint(1, 5)
    
def rand7():
    return (rand5()+rand5()+rand5()+rand5()+rand5()+rand5()+rand5()-7)%7
    # while (1):
    #     num = 5 * (random.randint(1, 5) - 1) + random.randint(1, 5)
    #     if (num < 22) : return (num % 7)

results = [0] * 7

for _i in range(200000):
    if rand7() == 0:
        results[0] += 1
    if rand7() == 1:
        results[1] += 1
    if rand7() == 2:
        results[2] += 1
    if rand7() == 3:
        results[3] += 1
    if rand7() == 4:
        results[4] += 1
    if rand7() == 5:
        results[5] += 1
    if rand7() == 6:
        results[6] += 1

print(results)