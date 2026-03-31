import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", A)
print("\nMatrix B:\n", B)


print("\nAddition:\n", A + B)


print("\nMultiplication:\n", np.dot(A, B))


print("\nTranspose of A:\n", A.T)
