#What is the index of the first term in the Fibonacci sequence to contain 1000 digits
import math
import decimal 
from math import sqrt
s5 = decimal.Decimal(5).sqrt()
def fib(n):
 f = long(((1+s5)**n - (1-s5)**n) / ((2**n)*s5))
 return f

for i in range (1,10000):
 if len(str(fib(i)))>=1000:
  print i, ':', fib(i)
  break
 
