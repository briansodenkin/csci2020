import numpy as np
import random
from time import time

def MatrixTransfer_Plain(M):
    MatrixTransfer = []
    for i in range(len(M)):
        MatrixTransfer.append(list(map(lambda x : x*i, M[i-1])))
    return MatrixTransfer

def MatrixTransfer_Numpy(M):
    tmp = np.arrange(M.shape[0])
    tmp = MatrixTransfer.reshape(-1,1)
    MatrixTransfer = MatrixTransfer * tmp
    return MatrixTransfer

n = 1000
m = 1000
Matrix_1 = [[random.random() for _ in range(m)] for _ in range(n)]
Matrix_1_np = np.random.rand(n, m)

t = time()
vec_3 = MatrixTransfer_Plain(Matrix_1)
print("Pythonic", time() - t)
t = time()
vec_4 = MatrixTransfer_Numpy(Matrix_1_np)
print("Numpy", time() - t)