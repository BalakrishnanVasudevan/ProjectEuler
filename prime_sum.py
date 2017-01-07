def isPrime(n):
 prime = True
 for i in range(2,n):
  if (n%i==0):
   prime = False 
 return prime

sum = 0
for x in range (2,2000000):
 print x, isPrime(x)
 if isPrime(x):
  sum = sum+x

print sum
