import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.signal as scp

plt.style.use("bmh")
sns.color_palette("husl", 8)

def linear_regresion(x, y):
    n = float(len(x))
    D = float(np.sum(np.square(x)) - (np.sum(x)**2)/n)
    E = float(np.sum(x*y) - np.sum(x)*np.sum(y)/n)
    F = float(np.sum(np.square(y)) - (np.sum(y)**2)/n)

    delta_m = np.sqrt((1/(n-2))*(D*F-E**2)/(D**2))
    delta_c = np.sqrt(1/(n-2)*(D/n+np.mean(x)**2)*(D*F-E**2)/(D**2))
    m = E/D
    c = np.mean(y)-m*np.mean(x)

    return m, c, delta_m, delta_c
    #using linear regression from Squires, with uncertainty to find slope and constant term


def equation_of_state(T, V):
    k   = 8.31   # Joule/kelvin/mol
    P_c = 33.6   # atm
    V_c = 0.089  # l/mol,
    T_c = 126    # K

    #T = T/T_c
    #V = V/V_c

    b = k*T_c/(8*P_c)
    a = P_c*27*b**2
    N = V_c/(3*b)

    return (N*k*T/(V-N*b) - a*N*N/(V*V))/P_c

"""
V_c = 0.089 # l/mol,
datapoints = int(1e5)
T = np.array([77, 100, 110, 115, 120, 125])
V = np.linspace(V_c/2.4, 7*V_c, datapoints)

for i in T:
    P = equation_of_state(i, V)
    plt.plot(V/V_c, P, label=r"$T=%3.0f$" % i)

plt.xlabel(r"Relative Volume $[\frac{V}{V_C}]$")
plt.ylabel(r"Relative Pressure $[\frac{P}{P_C}]$")
plt.axis([min(V/V_c), 4, -3, 5])
#plt.legend(loc='lower center', bbox_to_anchor=(0.5, 1.05),
#          ncol=3, fancybox=True, shadow=True)
plt.legend(loc="best", fontsize=12)
plt.savefig("figures/equation_of_state.pdf", bbox_inches="tight")
plt.show()
"""

V_c = 0.089 # l/mol,
datapoints = int(1e5)
T = np.array([77, 100, 110, 115, 120, 125])
#T = np.array([110, 115, 120])
V = np.linspace(V_c/2.4, 30*V_c, datapoints)

area = np.zeros(len(T))
V_g = np.zeros(len(T))
V_l = np.zeros(len(T))

dic = {}
dic["125"] = np.linspace(0.96, 0.97, 100)
dic["120"] = np.linspace(0.75, 0.85, 100)
dic["115"] = np.linspace(0.51, 0.75, 100)
dic["110"] = np.linspace(0.22, 0.66, 100)
dic["100"] = np.linspace(-0.4, 0.56, 100)
dic["77"]  = np.linspace(-2.5, 0.5, 100)


minimal_area_diff = 1e5
best_index = np.zeros(3, dtype=int)
counter = 0

for i in T:
    P = equation_of_state(i, V)
    plt.plot(V/V_c, P, label=r"$T=%3.0f$" % i)
    test_values = dic[str(i)]

    for test_value in test_values:
        indicies_MW = scp.argrelmin(abs(P-test_value))[0]

        if len(indicies_MW) > 2:
            volume_difference1 = test_value*(V[indicies_MW[1]]-V[indicies_MW[0]])/V_c
            volume_difference2 = test_value*(V[indicies_MW[2]]-V[indicies_MW[1]])/V_c

            area_1 = abs(volume_difference1 - np.trapz(P[indicies_MW[0]:indicies_MW[1]], V[indicies_MW[0]:indicies_MW[1]]/V_c))
            area_2 = abs(volume_difference2 - np.trapz(P[indicies_MW[1]:indicies_MW[2]], V[indicies_MW[1]:indicies_MW[2]]/V_c))


            area_diff = abs(area_1 - area_2)

            if area_diff < minimal_area_diff:
                best_index[0] = int(indicies_MW[0])
                best_index[1] = int(indicies_MW[1])
                best_index[2] = int(indicies_MW[2])

                best_test_value = test_value
                minimal_area_diff = area_diff

                area[counter] = area_diff
                V_g[counter] = V[indicies_MW[0]]/V_c
                V_l[counter] = V[indicies_MW[1]]/V_c

    plt.fill_between(V[best_index[0]:best_index[1]]/V_c, P[best_index[0]:best_index[1]], best_test_value* np.ones(best_index[1]-best_index[0]), alpha=0.25)

    plt.fill_between(V[best_index[1]:best_index[2]]/V_c, P[best_index[1]:best_index[2]], best_test_value* np.ones(best_index[2]-best_index[1]), alpha=0.25)

    plt.xlabel(r"Relative Volume $[\frac{V}{V_C}]$")
    plt.ylabel(r"Relative Pressure $[\frac{P}{P_C}]$")

    counter += 1
plt.axis([min(V/V_c), 4, -2.8, 1])
plt.legend(loc='lower center', bbox_to_anchor=(0.5, 1.05),
          ncol=3, fancybox=True, shadow=True)
#plt.legend(loc="best", fontsize=12)
#plt.savefig("figures/equation_of_state.pdf", bbox_inches="tight")
plt.show()

longer_T = np.linspace(75, 140, int(1e3))

m, c, delta_m, delta_c = linear_regresion(T, V_l-V_g)
plt.plot(T, V_l-V_g, "o")
plt.plot(longer_T, m*longer_T+c)

print(-c/m)
plt.show()
