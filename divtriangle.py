def fact(n):
 result = []
 for i in range (1,n+1):
  if n%i == 0:
   result.append(i)
 return len(result)
  

x = 0
for i in range(1,100000):
 x = x+i
 if fact(x) > 500:
  print x
  break

 
