import numpy as np
import matplotlib.pyplot as plt


def U(N, t, k, epsilon):
    return N*k/(t**2*(np.exp(1.0/t)-1)**2)*np.exp(1.0/t)


N = int(1e6)
t = np.linspace(0.1, 2, N)


energy = U(1, t, 1, 1)
plt.plot(t, energy)
plt.xlabel(r"Temperature [$kT/\epsilon$]")
plt.ylabel(r"Energy [$\frac{U}{Nk}$]")
plt.show()
