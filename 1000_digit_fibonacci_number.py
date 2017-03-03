import math
def count(n):
 if n > 0:
  digits = int(math.log10(n))+1
 elif n == 0:
  digits = 1
 else:
  digits = int(math.log10(-n))+2
 return digits

def fib(n):
 f1,f2 = -1,1
 fib = 0
 c = 0
 for i in range (1,n):
  fib = f1+f2
  print c, ':', fib
  if count(fib) >2:
   print '*******'
   print c, ':', fib
   break
  f1 = f2 
  f2= fib
  c+=1


fib(10)
