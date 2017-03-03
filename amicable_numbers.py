#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers. Evaluate the sum of all the amicable numbers under 10000.
def amicable(n):
 sum = 0
 for i in range(1,n):
  if (n % i == 0):
   sum = sum+i
 return sum

sum = 0
for i in range(1,10000):
 x = amicable(i)
 if (x != i) and (amicable(x) == i):
  print x, i
  sum = sum + i
print sum
