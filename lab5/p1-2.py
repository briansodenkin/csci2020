import numpy as np
import random
from time import time

def VMatrix_Plain(x, n):
    VMatrix = []
    for i in range(len(x)):
        tmp = []
        for j in range(n):
            tmp.append(x[i] ** j)
        VMatrix.append(tmp)
    return VMatrix

def VMatrix_Numpy(x, n):
    VMatrix = np.vander(x, n, True)
    return VMatrix

n = 1000
m = 500
x = [random.random() for _ in range(m)]
x_np = np.random.rand(m)


t = time()
vec_3 = VMatrix_Plain(x, n)
print("Pythonic", time() - t)
t = time()
vec_3 = VMatrix_Numpy(x_np, n)
print("Numpy", time() - t)
