import matplotlib.pyplot as plt
import numpy as np
import data

# Population size scatter plots
# Time plot
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.subplot(2, 1, 1)
plt.scatter(data.pop_x, data.y_poptime1)
plt.scatter(data.pop_x, data.y_poptime2)
plt.scatter(data.pop_x, data.y_poptime3)

plt.title("Population Size Graph")
#plt.xlabel("Population Size")
plt.ylabel("Computation Time (second)")

plt.grid(linestyle="--")
plt.legend(["Test 1", "Test 2", "Test 3"], loc="lower right")
plt.xticks(np.arange(0, 200, 10))
plt.yticks(np.arange(0, 0.12, 0.01))

# Length Plot
plt.subplot(2, 1, 2)
plt.scatter(data.pop_x, data.y_poplen1)
plt.scatter(data.pop_x, data.y_poplen2)
plt.scatter(data.pop_x, data.y_poplen3)

plt.xlabel("Population Size")
plt.ylabel("Path Length (meter)")

plt.grid(linestyle="--")
plt.legend(["Test 1", "Test 2", "Test 3"], loc="upper right")
plt.xticks(np.arange(0, 200, 10))

plt.show()


# Mutation rate scatter plots
# Time plot
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.subplot(2, 1, 1)
plt.scatter(data.mut_x, data.y_muttime1)
plt.scatter(data.mut_x, data.y_muttime2)
plt.scatter(data.mut_x, data.y_muttime3)

plt.title("Mutation Rate Graph")
#plt.xlabel("Population Size")
plt.ylabel("Computation Time (second)")

plt.grid(linestyle="--")
plt.legend(["Test 1", "Test 2", "Test 3"], loc="upper right")
plt.xticks(data.mut_x)

# Length Plot
plt.subplot(2, 1, 2)
plt.scatter(data.mut_x, data.y_mutlen1)
plt.scatter(data.mut_x, data.y_mutlen2)
plt.scatter(data.mut_x, data.y_mutlen3)

plt.xlabel("Mutation Rate")
plt.ylabel("Path Length (meter)")

plt.grid(linestyle="--")
plt.legend(["Test 1", "Test 2", "Test 3"], loc="upper right")
plt.xticks(data.mut_x)

plt.show()
