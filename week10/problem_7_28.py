import numpy as np
import matplotlib.pyplot as plt


def FD(eps, T, mu):
    k = 1
    return 1/(np.exp((eps-mu)/(k*T))+ 1)*eps


N = int(1e6)
mu = 1
eps = np.linspace(0, 4, N)
T = np.arange(0.2, 2.0, 0.01)

for temp in T:
    plt.plot(eps, FD(eps, temp, mu))

plt.show()
