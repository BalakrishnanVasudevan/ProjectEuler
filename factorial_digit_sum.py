#10 factorial is 3628800, and the sum of the digits in the number is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27. Find the sum of the digits in the number for 100 factorial
def fact(n):
 if n == 0:
  return 1
 else:
  return fact(n-1)*n

print fact(100)
a = list()
sum = 0
a = str(fact(100))
for i in range(0,len(a)):
 sum = sum + int(a[i])
print sum
