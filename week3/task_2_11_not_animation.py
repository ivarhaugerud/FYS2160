import numpy as np
import matplotlib.pyplot as plt

import scipy.misc as scm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter



def sigma_upp(N, N_1):
    return scm.comb(N, N_1)#N*np.log10(N)-N -  (N_1*np.log10(N_1)-N_1) - ((N-N_1)*np.log10(N-N_1)-(N-N_1))



Q_total = 1000
N = 10000
N_up = np.linspace(1, Q_total, Q_total)
sigma_N_upp_A = (sigma_upp(N, N_up))
sigma_N_upp_B = (sigma_upp(N, Q_total+1-N_up))
#answ = ((np.outer(sigma_N_upp_A, sigma_N_upp_A)))


plt.plot(N_up, sigma_N_upp_A+sigma_N_upp_B)
plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')
#ax.set_zlim(0, int(1500))

# Make data.
X, Y = np.meshgrid(N_up, N_up)
Z = answ

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                   linewidth=0, antialiased=False)

fig.colorbar(surf, shrink=0.5, aspect=5)

print("Number pointing up in most probable macro state:    %5.4f"    % N_up[int(np.mean(np.argmax(answ, axis=0)))])
print("With a probability of    :    %5.4f"    % np.sum(np.sum(answ)))


wframe = None
for phi in np.linspace(0, 180. / np.pi, 100):
    # If a line collection is already remove it before drawing.
    if wframe:
        ax.collections.remove(wframe)

    wframe = ax.plot_surface(X, Y, Z, rstride=2, cstride=2, cmap=cm.coolwarm)
    ax.view_init(30, phi)
    plt.pause(.001)
plt.show()
