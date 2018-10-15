import numpy as np
import matplotlib.pyplot as plt


from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter



def sigma_upp(N, N_1):
    return N*np.log(N)-N - (N_1*np.log(N_1)-N_1) - ((N-N_1)*np.log(N-N_1)-(N-N_1))


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_zlim(0, int(1500))

# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.set_zticklabels([])

for k in range(65):
    N = 2+k
    N_up = np.linspace(1, N-1, N-1)
    sigma_N_upp_A = (sigma_upp(N, N_up))
    sigma_N_upp_B = (sigma_upp(N, N_up))
    answ = np.outer(sigma_N_upp_A, sigma_N_upp_A)



    # Make data.
    X, Y = np.meshgrid(N_up, N_up)
    Z = answ#/np.max(np.max(answ))

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    #plt.draw()
    #plt.pause(0.01)
    plt.savefig("figures/%06d.png" % k)
#fig.colorbar(surf, shrink=0.5, aspect=5)
