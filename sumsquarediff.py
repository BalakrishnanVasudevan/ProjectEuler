#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
bsum = 0
for x in range(1,101):
 bsum = bsum+(x*x)
b = reduce(lambda a,c : a+c, range(1,101))
print b*b
print bsum
print b*b - bsum
