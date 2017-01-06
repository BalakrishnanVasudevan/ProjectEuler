#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
def fib(n):
 if n < 2:
  return n
 else:
  return fib(n-1) + fib(n-2)
a,x = 0, 0
for x in range (1,35): 
  print fib(x)
  if (fib(x)<4000000):
   if (fib(x) % 2 == 0):
    a += fib(x)
   x +=1
print a
