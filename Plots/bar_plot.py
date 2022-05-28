import matplotlib.pyplot as plt
import numpy as np
import data

# Population size
# Time plot
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.subplot(2, 1, 1)
plt.bar(data.pop_x, data.y_poptime1)
plt.bar(data.pop_x, data.y_poptime2)
plt.bar(data.pop_x, data.y_poptime3)

plt.title("Population Size Graph")
plt.ylabel("Computation Time (second)")

plt.grid(linestyle="--")
plt.legend(["Test 1", "Test 2", "Test 3"], loc="lower right")
#plt.yticks(np.arange(0, 0.055, 0.005))

# Length plot
plt.subplot(2, 1, 2)
plt.bar(data.pop_x, data.y_poplen1)
plt.bar(data.pop_x, data.y_poplen2)
plt.bar(data.pop_x, data.y_poplen3)

plt.title("Population Size Graph")
plt.ylabel("Computation Time (second)")

plt.grid(linestyle="--")
plt.legend(["Test 1", "Test 2", "Test 3"], loc="lower right")

plt.show()

""" # Mutation rate
# Time plot
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.subplot(2, 1, 1)
plt.bar(data.mut_x, data.y_muttime1)
plt.bar(data.mut_x, data.y_muttime2)
plt.bar(data.mut_x, data.y_muttime3)

plt.title("Mutation Rate Graph")
plt.ylabel("Computation Time (second)")

plt.grid(linestyle="--")
plt.legend(["Test 1", "Test 2", "Test 3"], loc="lower right")
plt.xticks(np.arange(0, 0.30, 0.01))

# Length plot
plt.subplot(2, 1, 2)
plt.bar(data.mut_x, data.y_mutlen1)
plt.bar(data.mut_x, data.y_mutlen2)
plt.bar(data.mut_x, data.y_mutlen3)

plt.title("Mutation Rate Graph")
plt.ylabel("Computation Time (second)")

plt.grid(linestyle="--")
plt.legend(["Test 1", "Test 2", "Test 3"], loc="lower right")

plt.show() """

# Chromosome length
# Time plot
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.subplot(2, 1, 1)
plt.bar(data.chr_x, data.y_chrtime1)
plt.bar(data.chr_x, data.y_chrtime2)
plt.bar(data.chr_x, data.y_chrtime3)

plt.title("Chromosome Length Graph")
plt.ylabel("Computation Time (second)")

plt.grid(linestyle="--")
plt.legend(["Test 1", "Test 2", "Test 3"], loc="lower right")
plt.yticks(np.arange(0, 0.055, 0.005))

# Length plot
plt.subplot(2, 1, 2)
plt.bar(data.chr_x, data.y_chrlen1)
plt.bar(data.chr_x, data.y_chrlen2)
plt.bar(data.chr_x, data.y_chrlen3)

plt.title("Chromosome Length Graph")
plt.ylabel("Computation Time (second)")

plt.grid(linestyle="--")
plt.legend(["Test 1", "Test 2", "Test 3"], loc="lower right")

plt.show()

# Stop Criteria
# Time plot
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.subplot(2, 1, 1)
plt.bar(data.st_x, data.y_sttime1)
plt.bar(data.st_x, data.y_sttime2)
plt.bar(data.st_x, data.y_sttime3)

plt.title("Stop Criteria Graph")
plt.ylabel("Computation Time (second)")

plt.grid(linestyle="--")
plt.legend(["Test 1", "Test 2", "Test 3"], loc="lower right")
#plt.yticks(np.arange(0, 0.055, 0.005))

# Length plot
plt.subplot(2, 1, 2)
plt.bar(data.st_x, data.y_stlen1)
plt.bar(data.st_x, data.y_stlen2)
plt.bar(data.st_x, data.y_stlen3)

plt.title("Stop Criteria Graph")
plt.ylabel("Computation Time (second)")

plt.grid(linestyle="--")
plt.legend(["Test 1", "Test 2", "Test 3"], loc="lower right")

plt.show()
