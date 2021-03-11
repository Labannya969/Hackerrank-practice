
import numpy

m,n=input().split()
c=numpy.array(([input().split() for _ in range(int(m))]),int)
print(numpy.mean(c, axis = 1) )
print(numpy.var(c, axis = 0) )

print(numpy.around(numpy.std(c), 11))


