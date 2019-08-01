"""
Monte Carlo methods

ratio of unit square circumscribed by a circle is :

.25 * pi / 1
"""
import random
print(random.random())

circle = 0
total = 0
pi = 3.141
answer = 0

while(abs(answer-pi) > .00099):

    for i in range(1000):
        x = random.random()
        y = random.random()

        if (x ** 2 + y ** 2 < 1) :
            # point lies within circle
            circle += 1
        
        total += 1

    answer = circle / total * 4
    print(answer)

print("total number of tries: ", circle + total)
