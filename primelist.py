#What is the 10001st prime number?
x = list()
for num in range(2,200000):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       x.append(num)
print x[10000]
