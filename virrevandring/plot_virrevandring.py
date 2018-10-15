import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation
import pandas as pd
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

#plt.style.use("bmh")
#sns.color_palette("hls", 1)

def get_data(filename, variables):
    df = pd.read_csv(filename,\
                    delim_whitespace=True, \
                    engine='python', \
                    names=variables)
    return df

number_of_files_read = 500
L = 30

data = {}
for i in range(number_of_files_read):
    data[str(i)] = get_data("data/data_"+str(int(i))+".txt", ['x', "y", "z"])
    for k in range(number_of_files_read):
        plt.draw


fig = plt.figure(4)
for k in range(number_of_files_read):
    plt.plot(np.array((data[str(k)]["x"])), np.array((data[str(k)]["y"])), linewidth=0.3)
plt.show()

fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
colours = ["b", "g", "r", "c", "m", "y", "k", "w"]

mpl.rcParams['legend.fontsize'] = 10

ax = fig.gca(projection='3d')
for k in range(number_of_files_read):
    ax.plot(np.array((data[str(k)]["x"])), np.array((data[str(k)]["y"])), np.array((data[str(k)]["z"])), linewidth=0.3)
plt.show()

fig = plt.figure(2)
ax = fig.gca(projection='3d')

for i in range(len(data[str(i)]["x"])):
    ax.cla()
    ax.set_xlim3d(-L, L)
    ax.set_ylim3d(-L, L)
    ax.set_zlim3d(-L, L)
    for k in range(number_of_files_read):
        ax.scatter(int(float(data[str(k)]["x"][i])), int(float(data[str(k)]["y"][i])), int(float(data[str(k)]["z"][i])))
    plt.pause(0.01)
plt.show()
