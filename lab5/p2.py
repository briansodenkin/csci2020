import numpy as np
import matplotlib.pyplot as plt

def plot(I, V):
    v_str = []
    for i in V:
        v_str.append(str(i))
    
    plt.bar(v_str, I)
    plt.xlabel("V (V)")
    plt.ylabel("I (A)")
    plt.savefig("bar.png")
    plt.clf()

def polyfit_np(I, V):
    