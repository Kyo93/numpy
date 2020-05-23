# Program to add two matrices using nested loop
import numpy as np

X = [[0, 1, 2],
     [3, 4, 5],
     [6, 7, 8]]

Y = [[8, 7, 6],
     [5, 4, 3],
     [2, 1, 0]]

result = np.zeros((3, 3))

# iterate through rows
for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)

# cách 2 sử dụng tiện ích của list trong python

result2 = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

for r in result2:
    print(r)
