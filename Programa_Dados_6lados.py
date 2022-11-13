from functools import reduce
import random

# This program is for calculating dice  rolls in RPG games.

# For example, rolling 3 six-sided dice.

d1 = sum(random.sample(range(1 , 6) , 1))
d2 = sum(random.sample(range(1 , 6) , 1))
d3 = sum(random.sample(range(1,  6) , 1))

d6 = d1 + d2 + d3

print(d1)
print(d2)
print(d3)

print('Summation: ' + str(d6) )