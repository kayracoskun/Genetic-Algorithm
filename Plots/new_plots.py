from matplotlib import pyplot as plt
import numpy as np
import data

""" POPULATION SIZE """
pop_time_av = np.zeros(np.shape(data.pop_x))
pop_len_av = np.zeros(np.shape(data.pop_x))

for i in range(len(pop_time_av)):
    pop_time_av[i] = (data.y_poptime1[i] +
                      data.y_poptime2[i] + data.y_poptime3[i]) / 3

for i in range(len(pop_len_av)):
    pop_len_av[i] = (data.y_poplen1[i] +
                     data.y_poplen2[i] + data.y_poplen3[i]) / 3

# Population size plots
# Time Plot
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.pop_x, pop_time_av, color="r")
plt.scatter(data.pop_x, data.y_poptime1, marker="*")
plt.scatter(data.pop_x, data.y_poptime2, marker="^")
plt.scatter(data.pop_x, data.y_poptime3, marker="o")

plt.title("Population Size - Computation Time Graph")
plt.ylabel("Computation Time (second)")
plt.xlabel("Population Size")

plt.grid(linestyle="--")
plt.legend(["Average", "Test 1", "Test 2", "Test 3"], loc="lower right")
plt.xticks(np.arange(0, 200, 10))
plt.yticks(np.arange(0.005, 0.11, 0.005))

plt.show()

# Length Plot
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.pop_x, pop_len_av, color="r")
plt.scatter(data.pop_x, data.y_poplen1, marker="*", s=150)
plt.scatter(data.pop_x, data.y_poplen2, marker="^", s=50)
plt.scatter(data.pop_x, data.y_poplen3, marker="o")

plt.title("Population Size - Path Length Graph")
plt.xlabel("Population Size")
plt.ylabel("Path Length (meter)")

plt.grid(linestyle="--")
plt.legend(["Average", "Test 1", "Test 2", "Test 3"], loc="upper right")
plt.xticks(np.arange(0, 200, 10))
plt.yticks(np.arange(7.8, 8.5, 0.05))

plt.show()

""" CHROMOSOME LENGTH """

chr_time_av = np.zeros(np.shape(data.chr_x))
chr_len_av = np.zeros(np.shape(data.chr_x))

for i in range(len(chr_time_av)):
    chr_time_av[i] = (data.y_chrtime1[i] +
                      data.y_chrtime2[i] + data.y_chrtime3[i]) / 3

for i in range(len(chr_len_av)):
    chr_len_av[i] = (data.y_chrlen1[i] +
                     data.y_chrlen2[i] + data.y_chrlen3[i]) / 3

# Chromosome length plots
# Time plots
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.chr_x, chr_time_av, color="r")
plt.scatter(data.chr_x, data.y_chrtime1, marker="*", s=150)
plt.scatter(data.chr_x, data.y_chrtime2, marker="^", s=50)
plt.scatter(data.chr_x, data.y_chrtime3, marker="o")

plt.title("Chromosome Length - Computation Time Graph")
plt.ylabel("Computation Time (second)")
plt.xlabel("Chromosome Length")

plt.grid(linestyle="--")
plt.legend(["Average", "Test 1", "Test 2", "Test 3"], loc="lower right")
plt.xticks(np.arange(9, 16, 1))
plt.yticks(np.arange(0.06, 0.135, 0.005))

plt.show()

# Length Plot
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.chr_x, chr_len_av, color="r")
plt.scatter(data.chr_x, data.y_chrlen1, marker="*", s=150)
plt.scatter(data.chr_x, data.y_chrlen2, marker="^", s=50)
plt.scatter(data.chr_x, data.y_chrlen3, marker="o")

plt.title("Chromosome Length - Path Length Graph")
plt.xlabel("Chromosome Length")
plt.ylabel("Path Length (meter)")

plt.grid(linestyle="--")
plt.legend(["Average", "Test 1", "Test 2", "Test 3"], loc="lower right")
plt.ylim([7.845, 7.860])
plt.xticks(np.arange(9, 16, 1))
plt.yticks(np.arange(7.845, 7.860, step=0.001))

plt.show()
