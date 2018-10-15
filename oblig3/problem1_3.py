import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

plt.style.use("bmh")
sns.color_palette("husl", 8)

def equation_of_state(T, V):
    k = 8.31 #Joule/kelvin/mol
    P_c = 33.6  # Pa
    V_c = 0.089 # l/mol,
    T_c = 126   #K

    T = T/T_c
    V = V/V_c

    b = k*T_c/(8*P_c)
    a = P_c*27*b**2
    N = V_c/(3*b)

    return (N*k*T/(V-N*b) - a*N*N/(V*V))/P_c

def ideal_gas(N, T, V_1, V_2):
    return N*k*T*np.log(V_1/V_2)

datapoints = int(1e5)
T = np.array([77, 100, 110, 115, 120, 125])
V = np.linspace(1, 20, datapoints)
V_c = 0.089 # l/mol,


for i in T:
    P = equation_of_state(i, V)*1e5
    plt.plot(V/V_c, P, label=r"$T=%3.0f$" % i)

plt.xlabel(r"Relative Volume $[\frac{V}{V_C}]$")
plt.ylabel(r"Relative Pressure $[\frac{P}{P_C}]\times 10^{5}$")
plt.axis([min(V/V_c), max(V/V_c), 0, 1.1*max(P)])
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
          ncol=3, fancybox=True, shadow=True)
plt.savefig("figures/equation_of_state.pdf", bbox_inches="tight")
plt.show()
