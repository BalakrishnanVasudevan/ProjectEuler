#Which starting number, under one million, produces the longest Collatz chain?
l = list()
max_list = list()
max_length = 0
for i in range (2,1000000):
 n = i
 l.append(n)
 while (n!=1):
  if (n%2 == 0):
   n = n/2
   l.append(n)
  else:
   n = 3*n + 1
   l.append(n)
 if len(l) > max_length:
  max_length = len(l)
  max_list = l[:]
 del l[:]
print max_list
print max_list[0]
print max_length
print len(max_list)

