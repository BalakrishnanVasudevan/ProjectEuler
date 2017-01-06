#smallest positive number that is evenly divisible by all of the numbers from 1 to 20
from operator import mul
from fractions import gcd
x = list()
for i in range(1,21):
 x.append(i)
print x
print reduce(lambda a,b: a * b / gcd(a,b), x)

