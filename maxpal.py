#Find the largest palindrome made from the product of two 3-digit numbers.
max = 100 
for i in range (1,1000):
 for j in range (1,1000):
  if (i*j > max):
   d = i*j
   x = str(d)
   y = x[::-1]
   if d == int(y):
    max = d
print max
