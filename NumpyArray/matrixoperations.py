import numpy as np

# cong 2 ma tran
A = np.array([[2, 4], [5, -6]])
B = np.array([[9, -3], [3, 6]])
C = A + B
print(C)

# nhan 2 ma tran

A = np.array([[3, 6, 7], [5, -3, 0]])
B = np.array([[1, 1], [2, 1], [3, -3]])
C = A.dot(B)
print(C)

# Chuyen vi ma tran
A = np.array([[1, 1], [2, 1], [3, -3]])
print(A.transpose())

# index

A = np.array([[1, 4, 5, 12],
              [-5, 8, 9, 0],
              [-6, 7, 11, 19]])

print("A[0][0] =", A[0][0])
print("A[1][2] =", A[1][2])
print("A[-1][-1] =", A[-1][-1])
# access rows and columns

print("A[0] = ", A[0])  # row 1
print('A[:,0]', A[:, 0])  # column 1

# Slicing of a Matrix

A = np.array([[1, 4, 5, 12, 14],
              [-5, 8, 9, 0, 17],
              [-6, 7, 11, 19, 21]])

print(A[:2, :4])  # two rows, four columns
print(A[:1, ])  # first row, all columns
print(A[:, 2])  # all rows, second column
print(A[:, 2:5])  # all rows, third to the fifth column
