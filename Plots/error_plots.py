from matplotlib import pyplot as plt
import numpy as np
import data

""" POPULATION SIZE """

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

plt.title("Population Size - Error Graph")
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
plt.legend(["Average", "Test 1", "Test 2", "Test 3"], loc="upper right")
plt.xticks(np.arange(0, 200, 10))

plt.show()

""" MUTATION RATE """

mut_time_av = (np.average(data.y_muttime1) +
               np.average(data.y_muttime2) + np.average(data.y_muttime3)) / 3

arr_mut_time_av = np.full(data.mut_x.shape, mut_time_av)

mut_len_av = (np.average(data.y_mutlen1) +
              np.average(data.y_mutlen2) + np.average(data.y_mutlen3)) / 3

arr_mut_len_av = np.full(data.mut_x.shape, mut_len_av)

# Mutation rate error plots
# Time Plot
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.subplot(2, 1, 1)
plt.plot(data.mut_x, arr_mut_time_av, color="r")
plt.scatter(data.mut_x, data.y_muttime1, marker="*")
plt.scatter(data.mut_x, data.y_muttime2, marker="^")
plt.scatter(data.mut_x, data.y_muttime3, marker="o")

plt.title("Mutation Rate - Error Graph")
plt.ylabel("Computation Time (second)")

plt.grid(linestyle="--")
plt.legend(["Average", "Test 1", "Test 2", "Test 3"], loc="upper right")

# Length Plot
plt.subplot(2, 1, 2)
plt.plot(data.mut_x, arr_mut_len_av, color="r")
plt.scatter(data.mut_x, data.y_mutlen1, marker="*")
plt.scatter(data.mut_x, data.y_mutlen2, marker="^")
plt.scatter(data.mut_x, data.y_mutlen3, marker="o")

plt.xlabel("Mutation Rate")
plt.ylabel("Path Length (meter)")

plt.grid(linestyle="--")
plt.legend(["Average", "Test 1", "Test 2", "Test 3"], loc="lower right")

plt.show()

""" STOP CRITERIA """

stop_time_av = (np.average(data.y_sttime1) +
                np.average(data.y_sttime2) + np.average(data.y_sttime3)) / 3

arr_stop_time_av = np.full(data.st_x.shape, stop_time_av)

stop_len_av = (np.average(data.y_stlen1) +
               np.average(data.y_stlen2) + np.average(data.y_stlen3)) / 3

arr_stop_len_av = np.full(data.st_x.shape, stop_len_av)

# Stop criterion line plots
# Time plots
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.subplot(2, 1, 1)
plt.plot(data.st_x, arr_stop_time_av, color="r")
plt.scatter(data.st_x, data.y_sttime1, marker="*")
plt.scatter(data.st_x, data.y_sttime2, marker="^")
plt.scatter(data.st_x, data.y_sttime3, marker="o")

plt.title("Stop Criterion - Error Graph")
plt.ylabel("Computation Time (second)")

plt.grid(linestyle="--")
plt.legend(["Average", "Test 1", "Test 2", "Test 3"], loc="lower right")

# Length Plot
plt.subplot(2, 1, 2)
plt.plot(data.st_x, arr_stop_len_av, color="r")
plt.scatter(data.st_x, data.y_stlen1, marker="*")
plt.scatter(data.st_x, data.y_stlen2, marker="^")
plt.scatter(data.st_x, data.y_stlen3, marker="o")

plt.xlabel("Stop Criterion")
plt.ylabel("Path Length (meter)")

plt.grid(linestyle="--")
plt.legend(["Average", "Test 1", "Test 2", "Test 3"], loc="lower right")

plt.show()

""" CHROMOSOME LENGTH """

chr_time_av = (np.average(data.y_chrtime1) +
               np.average(data.y_chrtime2) + np.average(data.y_chrtime3)) / 3

arr_chr_time_av = np.full(data.chr_x.shape, chr_time_av)

chr_len_av = (np.average(data.y_chrlen1) +
              np.average(data.y_chrlen2) + np.average(data.y_chrlen3)) / 3

arr_chr_len_av = np.full(data.chr_x.shape, chr_len_av)

# Chromosome length line plots
# Time plots
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.subplot(2, 1, 1)
plt.plot(data.chr_x, arr_chr_time_av, color="r")
plt.scatter(data.chr_x, data.y_chrtime1, marker="*")
plt.scatter(data.chr_x, data.y_chrtime2, marker="^")
plt.scatter(data.chr_x, data.y_chrtime3, marker="o")

plt.title("Chromosome Length - Error Graph")
plt.ylabel("Computation Time (second)")

plt.grid(linestyle="--")
plt.legend(["Average", "Test 1", "Test 2", "Test 3"], loc="lower right")

# Length Plot
plt.subplot(2, 1, 2)
plt.plot(data.chr_x, arr_chr_len_av, color="r")
plt.scatter(data.chr_x, data.y_chrlen1, marker="*")
plt.scatter(data.chr_x, data.y_chrlen2, marker="^")
plt.scatter(data.chr_x, data.y_chrlen3, marker="o")

plt.xlabel("Chromosome Length")
plt.ylabel("Path Length (meter)")

plt.grid(linestyle="--")
plt.legend(["Average", "Test 1", "Test 2", "Test 3"], loc="lower right")

plt.show()
