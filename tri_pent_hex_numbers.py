for i in range (285,10000):
 for j in range (165,10000):
  for k in range (143,10000):
   x = (i*(i+1)/2)
   y = (j*((3*j)-1)/2)
   z = (k*((2*k)-1))
   if x == y == z:
    print i, j, k, x
