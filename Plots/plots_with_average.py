import data
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"

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
plt.scatter(data.pop_x, data.y_poptime1, marker="*", s=200)
plt.scatter(data.pop_x, data.y_poptime2, marker="^", s=70)
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
plt.scatter(data.pop_x, data.y_poplen1, marker="*", s=200)
plt.scatter(data.pop_x, data.y_poplen2, marker="^", s=70)
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
plt.scatter(data.chr_x, data.y_chrtime1, marker="*", s=200)
plt.scatter(data.chr_x, data.y_chrtime2, marker="^", s=70)
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
plt.scatter(data.chr_x, data.y_chrlen1, marker="*", s=200)
plt.scatter(data.chr_x, data.y_chrlen2, marker="^", s=70)
plt.scatter(data.chr_x, data.y_chrlen3, marker="o")

plt.title("Chromosome Length - Path Length Graph")
plt.xlabel("Chromosome Length")
plt.ylabel("Path Length (meter)")

plt.grid(linestyle="--")
plt.legend(["Average", "Test 1", "Test 2", "Test 3"], loc="lower right")
plt.ylim([7.852, 7.856])
plt.xticks(np.arange(9, 16, 1))
plt.yticks(np.arange(7.852, 7.857, step=0.001))

plt.show()

""" STOP CRITERION """

st_time_av = np.zeros(np.shape(data.st_x))
st_len_av = np.zeros(np.shape(data.st_x))

for i in range(len(st_time_av)):
    st_time_av[i] = (data.y_sttime1[i] +
                     data.y_sttime2[i] + data.y_sttime3[i]) / 3

for i in range(len(st_len_av)):
    st_len_av[i] = (data.y_stlen1[i] +
                    data.y_stlen2[i] + data.y_stlen3[i]) / 3

# Stop criterion line plots
# Time plots
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.st_x, st_time_av, color="r")
plt.scatter(data.st_x, data.y_sttime1, marker="*", s=200)
plt.scatter(data.st_x, data.y_sttime2, marker="^", s=70)
plt.scatter(data.st_x, data.y_sttime3, marker="o")

plt.title("Stop Criterion - Compution Time Graph")
plt.xlabel("Stop Criterion")
plt.ylabel("Computation Time (second)")

plt.grid(linestyle="--")
plt.legend(["Average", "Test 1", "Test 2", "Test 3"], loc="lower right")
plt.xticks(np.arange(2, 7, 1))
plt.yticks(np.arange(0.03, 0.08, step=0.005))

plt.show()

# Length Plot
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.st_x, st_len_av, color="r")
plt.scatter(data.st_x, data.y_stlen1, marker="*", s=200)
plt.scatter(data.st_x, data.y_stlen2, marker="^", s=70)
plt.scatter(data.st_x, data.y_stlen3, marker="o")

plt.title("Stop Criterion - Path Length Graph")
plt.xlabel("Stop Criterion")
plt.ylabel("Path Length (meter)")

plt.grid(linestyle="--")
plt.legend(["Average", "Test 1", "Test 2", "Test 3"], loc="lower right")
plt.ylim([7.852, 7.856])
plt.yticks(np.arange(7.852, 7.857, step=0.001))
plt.xticks(np.arange(2, 7, 1))

plt.show()

""" MUTATION RATE """

mut_time_av = np.zeros(np.shape(data.mut_x))
mut_len_av = np.zeros(np.shape(data.mut_x))

for i in range(len(mut_time_av)):
    mut_time_av[i] = (data.y_muttime1[i] +
                      data.y_muttime2[i] + data.y_muttime3[i]) / 3

for i in range(len(mut_len_av)):
    mut_len_av[i] = (data.y_mutlen1[i] +
                     data.y_mutlen2[i] + data.y_mutlen3[i]) / 3

# Mutation rate plots
# Time Plot
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.mut_x, mut_time_av, color="r")
plt.scatter(data.mut_x, data.y_muttime1, marker="*", s=200)
plt.scatter(data.mut_x, data.y_muttime2, marker="^", s=70)
plt.scatter(data.mut_x, data.y_muttime3, marker="o")

plt.title("Mutation Rate - Computation Time Graph")
plt.xlabel("Mutation Rate")
plt.ylabel("Computation Time (second)")

plt.grid(linestyle="--")
plt.legend(["Average", "Test 1", "Test 2", "Test 3"], loc="upper right")
plt.xticks(np.arange(0, 0.275, 0.025))

plt.show()

# Length Plot
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.mut_x, mut_len_av, color="r")
plt.scatter(data.mut_x, data.y_mutlen1, marker="*", s=200)
plt.scatter(data.mut_x, data.y_mutlen2, marker="^", s=70)
plt.scatter(data.mut_x, data.y_mutlen3, marker="o")

plt.title("Mutation Rate - Path Length Graph")
plt.xlabel("Mutation Rate")
plt.ylabel("Path Length (meter)")

plt.grid(linestyle="--")
plt.legend(["Average", "Test 1", "Test 2", "Test 3"], loc="lower right")
plt.ylim([7.852, 7.856])
plt.yticks(np.arange(7.852, 7.857, step=0.001))
plt.xticks(np.arange(0, 0.275, 0.025))

plt.show()
