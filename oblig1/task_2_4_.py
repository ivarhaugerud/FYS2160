import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import seaborn as sns
plt.style.use("bmh")
sns.color_palette("hls", 1)

def find_total_spin(M, number):
    array = number - 2*np.sum(np.random.randint(0, 2, (M, number)), axis=1)
    return array

def analytical_distribution(S, N):
    return np.exp(-S**2.0/(2.0*N))*np.sqrt(2.0/(np.pi*N))

M = int(1e4)
N = int(60)
M_array = np.linspace(1, M, M)
answer = find_total_spin(M, N)/2.0

"""
plt.scatter(np.linspace(1, M, M), answer, s=2.5, c="green", label="Measurments")
plt.xlabel(r"Microstate #")
plt.ylabel(r"Total spin $S$")
plt.plot(M_array, np.mean(answer)*np.ones(M), "--", label=r"Average = %4.3f" %  (np.mean(answer)))
plt.legend(loc="best")
plt.savefig("figure/task_2_3.pdf")
plt.show()
"""

bin_array = np.arange(int(min(answer)), int(max(answer)))-0.5
number_of_bins = int(max(answer))-int(min(answer))+1
print(number_of_bins)
plt.hist(answer, number_of_bins)#, normed=1, facecolor='green', alpha=0.75, edgecolor = 'black', label="measurments")
#mu, sigma = np.mean(answer), np.std(answer)
#y = mlab.normpdf(bins, mu, sigma)
#l = plt.plot(bins, y, 'r--', linewidth=1, label="gaussian distribution")

plt.ylabel(r"Probability")
plt.xlabel(r"Total spin $S$")
#plt.axis([-np.max(abs(answer)), np.max(abs(answer)), 0, 0.11])
plt.legend(loc="best")
plt.savefig("figure/histogram.pdf")
plt.show()

"""
n, bins, patches = plt.hist(answer, np.arange(min(answer), max(answer))-0.5, normed=1, facecolor='green', alpha=0.75, edgecolor = 'black', label="measurments")
mu = np.mean(answer)
sigma = np.std(answer)

y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r--', linewidth=1, label="gaussian distribution")

S_array = np.linspace(-N, N, N*2+1)
analytical = analytical_distribution(S_array, N=60)
plt.plot(S_array, analytical, label="analytical distribution")

plt.ylabel(r"Probability")
plt.xlabel(r"Total spin $S$")
#plt.axis([-np.max(abs(answer)), np.max(abs(answer)), 0, 0.11])
plt.legend(loc="best")
plt.savefig("figure/task_2_6.pdf")
plt.show()
"""
