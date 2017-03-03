#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2
def pal(n):
 x = str(n)
 y = x[::-1]
 if n == int(y):
  return True
 else:
  return False

sum = 0
for i in range(1,1000000):
 if pal(i) and pal(int(bin(i)[2:])):
  print i, int(bin(i)[2:])
  sum = sum + i
print sum
 
