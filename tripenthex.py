
m = [(i*(i+1))/2 for i in range(2,100000)]
n = [(i*((3*i)-1)/2) for i in range (2,100000)]
o = [(i*((2*i)-1)) for i in range(2,100000)]
e = set(m) & set(n) & set(o)
print e
