from matplotlib import pyplot as plt
import numpy as np
import data

# Population size line plots
# Time Plot
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.subplot(2, 1, 1)
plt.plot(data.pop_x, data.y_poptime1, data.pop_x,
         data.y_poptime2, data.pop_x, data.y_poptime3, marker="o")

plt.title("Population Size Graph")
#plt.xlabel("Population Size")
plt.ylabel("Computation Time (second)")

plt.grid(linestyle="--")
plt.legend(["Test 1", "Test 2", "Test 3"], loc="lower right")
plt.xticks(np.arange(0, 200, 10))
plt.yticks(np.arange(0, 0.12, 0.01))

# Length Plot
plt.subplot(2, 1, 2)
plt.plot(data.pop_x, data.y_poplen1, data.pop_x,
         data.y_poplen2, data.pop_x, data.y_poplen3, marker="o")

plt.xlabel("Population Size")
plt.ylabel("Path Length (meter)")

plt.grid(linestyle="--")
plt.legend(["Test 1", "Test 2", "Test 3"], loc="lower right")
plt.xticks(np.arange(0, 200, 10))

plt.show()


# Mutation rate line plots
# Time plots
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.subplot(2, 1, 1)
plt.plot(data.mut_x, data.y_muttime1, data.mut_x,
         data.y_muttime2, data.mut_x, data.y_muttime3, marker="o")

plt.title("Mutation Rate Graph")
#plt.xlabel("Population Size")
plt.ylabel("Computation Time (second)")

plt.grid(linestyle="--")
plt.legend(["Test 1", "Test 2", "Test 3"], loc="upper right")

# Length Plot
plt.subplot(2, 1, 2)
plt.plot(data.mut_x, data.y_mutlen1, data.mut_x,
         data.y_mutlen2, data.mut_x, data.y_mutlen3, marker="o")

plt.xlabel("Mutation Rate")
plt.ylabel("Path Length (meter)")

plt.grid(linestyle="--")
plt.legend(["Test 1", "Test 2", "Test 3"], loc="lower right")

plt.show()


# Chromosome length line plots
# Time plots
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.subplot(2, 1, 1)
plt.plot(data.chr_x, data.y_chrtime1, data.chr_x,
         data.y_chrtime2, data.chr_x, data.y_chrtime3, marker="o")

plt.title("Chromosome Length Graph")
#plt.xlabel("Population Size")
plt.ylabel("Computation Time (second)")

plt.grid(linestyle="--")
plt.legend(["Test 1", "Test 2", "Test 3"], loc="lower right")

# Length Plot
plt.subplot(2, 1, 2)
plt.plot(data.chr_x, data.y_chrlen1, data.chr_x,
         data.y_chrlen2, data.chr_x, data.y_chrlen3, marker="o")

plt.xlabel("Chromosome Length")
plt.ylabel("Path Length (meter)")

plt.grid(linestyle="--")
plt.legend(["Test 1", "Test 2", "Test 3"], loc="lower right")

plt.show()


# Stop criteria line plots
# Time plots
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.subplot(2, 1, 1)
plt.plot(data.st_x, data.y_sttime1, data.st_x,
         data.y_sttime2, data.st_x, data.y_sttime3, marker="o")

plt.title("Stop Criteria Graph")
#plt.xlabel("Population Size")
plt.ylabel("Computation Time (second)")

plt.grid(linestyle="--")
plt.legend(["Test 1", "Test 2", "Test 3"], loc="lower right")

# Length Plot
plt.subplot(2, 1, 2)
plt.plot(data.st_x, data.y_stlen1, data.st_x,
         data.y_stlen2, data.st_x, data.y_stlen3, marker="o")

plt.xlabel("Stop Criteria")
plt.ylabel("Path Length (meter)")

plt.grid(linestyle="--")
plt.legend(["Test 1", "Test 2", "Test 3"], loc="lower right")

plt.show()
