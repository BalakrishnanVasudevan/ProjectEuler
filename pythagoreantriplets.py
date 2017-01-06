#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2+b^2 = c^2, There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
for a in range (1,998):
 for b in range (2,998):
  for c in range(3,998):
   if (a<b) and (a<c) and (b<c) and (a**2+b**2 == c**2) and (a+b+c == 1000):
     print 'pythagorean triplets: ',a,b,c
     print 'product: ', a*b*c
