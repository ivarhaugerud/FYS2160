import numpy as np
import matplotlib.pyplot as plt
import math as math

def calcer(N, n):
    return math.factorial(N)/(math.factorial(n)*math.factorial(N-n))

N = 1000
n = np.zeros(N+1)
probability = np.zeros(N+1)

for i in range(len(n)):
    n[i] = i
    probability[i] = calcer(N, n[i])

probability = probability/2**N

plt.semilogy(n, (probability))
plt.show()
