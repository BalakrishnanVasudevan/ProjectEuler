#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
def fact(n):
 num = 1
 while n > 1:
  num = num * n
  n = n-1
 return num

x = 0
for i in range (3,1000000):
 a = list()
 b = i
 a = str(b)
 sum = 0
 for k in range(0,len(a)):
  sum = sum + fact(int(a[k]))
 if sum == i:
  print i 
  x = x+i
print 'sum: ', x

