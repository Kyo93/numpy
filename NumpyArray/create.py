import numpy as np

A = np.array([[1, 2, 3], [3, 4, 5]])
print(A)

A = np.array([[1.1, 2, 3], [3, 4, 5]])  # Array of floats
print(A)

A = np.array([[1, 2, 3], [3, 4, 5]], dtype=complex)  # Array of complex numbers
print(A)

zeros_array = np.zeros((2, 3))
print(zeros_array)

ones_array = np.ones((1, 5), dtype=np.int32)  # specifying dtype
print(ones_array)

##Using arange() and shape()

A = np.arange(4)
print('A =', A)

B = np.arange(12).reshape(2, 6)
print('B =', B)
