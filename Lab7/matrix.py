import numpy

N, M = map(int, input().split())
A = numpy.array([input().split() for i in range(N)], dtype =int)
print(numpy.mean(A, axis =1))
print(numpy.var(A, axis =0))
print(numpy.std(A, axis = None))