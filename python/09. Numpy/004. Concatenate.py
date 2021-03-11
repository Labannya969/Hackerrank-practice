


import numpy


a,b,c=map(int,input().split())
arra=numpy.array([input().split() for _ in range(a)],int)
arrb=numpy.array([input().split() for _ in range(b)],int)
print(numpy.concatenate((arra, arrb), axis = 0))

