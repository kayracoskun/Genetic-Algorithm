from turtle import color
from matplotlib import pyplot as plt
import numpy as np
import data

pop_time_av = (np.average(data.y_poptime1) +
               np.average(data.y_poptime2) + np.average(data.y_poptime3)) / 3

arr_pop_time_av = np.full(data.pop_x.shape, pop_time_av)

pop_len_av = (np.average(data.y_poplen1) +
              np.average(data.y_poplen2) + np.average(data.y_poplen3)) / 3

arr_pop_len_av = np.full(data.pop_x.shape, pop_len_av)

# Population size line plots
# Time Plot
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.subplot(2, 1, 1)
plt.plot(data.pop_x, arr_pop_time_av, color="r")
plt.scatter(data.pop_x, data.y_poptime1, marker="*")
plt.scatter(data.pop_x, data.y_poptime2, marker="^")
plt.scatter(data.pop_x, data.y_poptime3, marker="o")

plt.title("Population Size Graph")
#plt.xlabel("Population Size")
plt.ylabel("Computation Time (second)")

plt.grid(linestyle="--")
plt.legend(["Average", "Test 1", "Test 2", "Test 3"], loc="lower right")
plt.xticks(np.arange(0, 200, 10))
plt.yticks(np.arange(0, 0.12, 0.01))

# Length Plot
plt.subplot(2, 1, 2)
plt.plot(data.pop_x, arr_pop_len_av, color="r")
plt.scatter(data.pop_x, data.y_poplen1, marker="*")
plt.scatter(data.pop_x, data.y_poplen2, marker="^")
plt.scatter(data.pop_x, data.y_poplen3, marker="o")

plt.xlabel("Population Size")
plt.ylabel("Path Length (meter)")

plt.grid(linestyle="--")
plt.legend(["Average", "Test 1", "Test 2", "Test 3"], loc="lower right")
plt.xticks(np.arange(0, 200, 10))

plt.show()
