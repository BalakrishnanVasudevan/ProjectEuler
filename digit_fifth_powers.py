#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
s = 0
for i in range (2,1000000):
 a = list()
 sum = 0
 a = str(i)
 for j in range(0, len(a)):
  sum = sum + int(a[j])**5
 if i == sum:
  s = s+i
  print i
print s

