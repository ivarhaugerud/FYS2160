import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as scm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
#import seaborn as sns
#plt.style.use("bmh")
#sns.color_palette("hls", 1)

def get_entropy(N, S):
    kb = 8.6173303*1e-5 #Ev/K
    return kb*(np.log(2)*N-S**2/(2*N)+np.log(np.sqrt(2*np.pi/N)))

number_of_particles = 120
number_of_Ns = number_of_particles+1
N = np.linspace(1, number_of_particles, number_of_Ns)
sigma = np.zeros((number_of_Ns, number_of_particles+1))

for i in range(number_of_Ns):
    S = np.linspace(0, N[i], N[i]+1)
    sigma[i, :int(N[i]+1)] = get_entropy(N[i], S)

S = np.linspace(0, number_of_particles, number_of_particles+1)


S_both = np.linspace(-number_of_particles, number_of_particles, 2*number_of_particles+1)
Ent_both = get_entropy(number_of_particles, S_both)
plt.plot(S_both, Ent_both*1e3)
plt.xlabel(r"Total spin $S$")
plt.ylabel(r"Entropy [m eV/K]")
plt.savefig("figure/task_2_7_1.pdf")
plt.show()


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X, Y = np.meshgrid(S, N)
Z = sigma*1e3

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)#linewidth=0, antialiased=False)
surf = ax.plot_surface(-X, Y, Z, cmap=cm.coolwarm)#linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.ylabel("Number of atoms")
plt.xlabel("Total spin")
ax.set_zlabel("Entropy [mEv/K]")
wframe = None

print("Largest entropy          :    %5.4f Ev/K"  % np.max(np.max(Z)*1e-3))

for phi in np.linspace(45, 45+180, 100):
    # If a line collection is already remove it before drawing.
    if wframe:
        ax.collections.remove(wframe)

    wframe = ax.plot_surface(X, Y, Z, rstride=2, cstride=2, cmap=cm.coolwarm)
    ax.view_init(30, -phi)
    plt.savefig("figure/%06d.pdf" % phi)
    plt.pause(.001)
plt.show()
