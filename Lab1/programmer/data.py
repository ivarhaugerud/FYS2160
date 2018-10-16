import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

plt.style.use("bmh")
sns.color_palette("husl", 8)
#sns.hls_palette(8, l=.3, s=.8)

#linear regression function
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



L = 1244*1e-3 #m

freq = np.array([311, 442, 592, 733, 877, 1020, 1164, 1309, 1454, 1598, 1744, 1887])
x = np.linspace(1, len(freq), len(freq))

m, c, delta_m, delta_c = linear_regresion(x, freq)
print(2*L*m, delta_m)

plt.ylabel("frekvens [Hz]")
plt.xlabel(r"måling nummer, $n$")
plt.plot(x, c+x*m, label="lineærregresjon, stigningstall: %3.1f(%i)" % (m, int(delta_m*10+1)))
plt.plot(x, freq, "o", label="målinger")
plt.savefig("measurements.png")
plt.legend(loc="best")
plt.show()

#T = 273.15 + 43.15 #hot air
#T = 273.15 + 23.1  #cold air
T = 273.15 + 23.1  #argon
#T = 273.15 + 22.7  #CO2
R = 8.3144598
#Mmol = 28.966/1000.0 #air
Mmol = 39.948/1000.0 #argon
#Mmol = 44.01/1000.0 #CO2
f = 3
c_id = np.sqrt((f+2)*R*T/(f*Mmol))
print("c ideal: ", c_id)
#print("c empiercal:", 2*L*m)
