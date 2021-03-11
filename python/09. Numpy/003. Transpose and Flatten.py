

import numpy

m,n=input().split()
b=numpy.array([input().split() for _ in range(int(m))],int)

print (numpy.transpose(b))
print (b.flatten())

