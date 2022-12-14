import numpy as np
import random
from time import time

def MatrixMultiple_Plain(M1, M2):
    # input M1 and M2 are lists of lists.
    M3 = []
    for i in range(len(M1)):
        row = []
        for j in range(len(M2)):
            tmp = 0
            for k in range(len(M1)):
                tmp += M1[i][k] * M2[k][j]
            row.append(tmp)
        M3.append(row)
    return M3

def MatrixMultiple_Numpy(M1, M2):
    # input M1 and M2 are 2d arrases.
    M3 = np.matmul(M1,M2)
    return M3


# n may vary
n = 1000
Matrix_1 = [[random.random() for _ in range(n)] for _ in range(n)]
Matrix_2 = [[random.random() for _ in range(n)] for _ in range(n)]
Matrix_1_np = np.random.rand(n, n)
Matrix_2_np = np.random.rand(n, n)

t = time()
vec_3 = MatrixMultiple_Plain(Matrix_1, Matrix_2)
print("Pythonic", time() - t)
t  = time()
vec_3 = MatrixMultiple_Numpy(Matrix_1_np, Matrix_2_np)
print("Numpy", time() - t)

