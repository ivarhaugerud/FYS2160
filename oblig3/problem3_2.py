import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

plt.style.use("bmh")
sns.color_palette("husl", 8)

def MaxwellDistribution(T, v, m):
    k = 8.31
    kT = k*T

    return (m/(2*np.pi*kT))**(3./2)*4*np.pi*v**2*np.exp(-m*v**2/(2*kT))

N = int(1e5)
v = np.linspace(0, 2000, N)
mass_nitrogen = 0.028


dist_300 =  MaxwellDistribution(300, v, mass_nitrogen)
dist_600 =  MaxwellDistribution(600, v, mass_nitrogen)


#TASK 3.2
plt.plot(v, dist_300*100, label=r"$T=300$K")
plt.plot(v, dist_600*100, label=r"$T=600$K")
plt.xlabel(r"Velocity $v$ [m/s]")
plt.ylabel(r"Probability [%]")

plt.legend(loc='upper right',
          ncol=1, fancybox=True, shadow=True, fontsize=12)
plt.savefig("figures/MaxwellDistribution.pdf", bbox_inches="tight")
plt.show()

#TASK 3.3
arg_300 = np.argmin(abs(v-300))
prob_less_than_300 = np.trapz(dist_300[:arg_300], v[:arg_300])
print()
print("TASK 3.3")
print("Probability of observing particle with speed less than 300m/s: ", prob_less_than_300*100)
print()

#TASK 3.4
v = np.linspace(0, 20000, 1e6)
escape_velocity = 11*1e3 #m/s
atmosphere_T = 1000 #K
dist_1000 =  MaxwellDistribution(atmosphere_T, v, mass_nitrogen)
arg_11000 = np.argmin(abs(v-escape_velocity))
prob_more_than_11000 = np.trapz(dist_1000[arg_11000:], v[arg_11000:])
print()
print("TASK 3.4")
print("Probability of observing particle with speed more than 11 000 m/s: ", prob_more_than_11000*100)
print()

#TASK 3.5
hydrogen_mass = 0.002
helium_mass   = 0.004
v = np.linspace(0, 20000, 1e6) #m/s

dist_hydrogen =  MaxwellDistribution(atmosphere_T, v, hydrogen_mass)
dist_helium =  MaxwellDistribution(atmosphere_T, v, helium_mass)

arg_11000 = np.argmin(abs(v-escape_velocity))
prob_hydrogen = np.trapz(dist_hydrogen[arg_11000:], v[arg_11000:])
prob_helium   = np.trapz(dist_helium[arg_11000:],   v[arg_11000:])
print()
print("TASK 3.5")
print("Probability of observing hydrogen with speed more than 11 000 m/s: ", prob_hydrogen*100)
print("Probability of observing helium   with speed more than 11 000 m/s: ", prob_helium*100)
print()



#TASK 3.6
v = np.linspace(0, 10000, 1e6)
escape_velocity = 2.4*1e3 #m/s
atmosphere_T = 1000 #K
dist_1000 =  MaxwellDistribution(atmosphere_T, v, mass_nitrogen)
arg_esc_vel = np.argmin(abs(v-escape_velocity))

prob_more_than_11000 = np.trapz(dist_1000[arg_esc_vel:], v[arg_esc_vel:])
print()
print("TASK 3.6")
print("Probability of observing nitrogen with speed more than 11 000 m/s on the moon: ", prob_more_than_11000*100)
print()
