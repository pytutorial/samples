import numpy

X = numpy.array([1,2,3,4])
print('X=', X)

print()
X2 = numpy.array([[1,2],[3,4]])
print('X2=\n', X2)

print()
X3 = numpy.ones(4)
print('X3=', X3)

print()
X4 = numpy.zeros((2,2), dtype=numpy.uint8)
print('X4=\n', X4, '\nX4 shape=', X4.shape, 'X4 data type:', X4.dtype)

print()
print('X4.reshape((1, 4)=', X4.reshape((1, 4)))

print()
X5 = numpy.ones((2,2), dtype=numpy.uint8)
print('X5=\n', X5)

print()
X6 = numpy.concatenate((X4, X5))
print('X6=\n', X6)

print()
X7 = numpy.array([[1,2],[3,4]])
print('X7[:,0]=', X7[:, 0])
print('X7[1, :]=', X7[1, :])

print()
X8 = numpy.array([[1,2],[3,4]])
X9 = numpy.array([[5,6],[7,8]])
print('X8 + X9=\n', X8 + X9)
print('X8 * X9=\n', X8 * X9)

print()
print('sum(X7)=', sum(X7))
print('mean(X8, axis=0)', numpy.mean(X8, axis=0))
print('mean(X8, axis=1)', numpy.mean(X8, axis=1))

print()
indexes = (X7 >= 2) & (X8 % 2 == 0)
print('(X7 >= 2) & (X8 % 2 == 0) : \n', indexes)

print()
print('X7[indexes]=', X7[indexes])
