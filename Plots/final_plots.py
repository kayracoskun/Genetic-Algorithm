from matplotlib import pyplot as plt
import numpy as np
import data

""" # Population size line plots
# Time Plot
# 1
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.pop_x, data.y_poptime1, marker="o")

plt.title("Population Size Graph 1")
plt.ylabel("Computation Time (second)")
plt.xlabel("Population Size")

plt.grid(linestyle="--")
plt.legend(["Test 1"], loc="lower right")
plt.xticks(np.arange(0, 200, 10))
plt.yticks(np.arange(0, 0.12, 0.005))

# 2
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.pop_x, data.y_poptime2, marker="o", color="orange")

plt.title("Population Size Graph 2")
plt.ylabel("Computation Time (second)")
plt.xlabel("Population Size")

plt.grid(linestyle="--")
plt.legend(["Test 2"], loc="lower right")
plt.xticks(np.arange(0, 200, 10))
plt.yticks(np.arange(0, 0.12, 0.005))

# 3
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.pop_x, data.y_poptime3, marker="o", color="green")

plt.title("Population Size Graph 3")
plt.ylabel("Computation Time (second)")
plt.xlabel("Population Size")

plt.grid(linestyle="--")
plt.legend(["Test 3"], loc="lower right")
plt.xticks(np.arange(0, 200, 10))
plt.yticks(np.arange(0, 0.12, 0.005))

# Time Plot
# 1
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.pop_x, data.y_poplen1, marker="o")

plt.title("Population Size Graph 1")
plt.ylabel("Path Length (meter)")
plt.xlabel("Population Size")

plt.grid(linestyle="--")
plt.legend(["Test 1"], loc="upper right")
plt.xticks(np.arange(0, 200, 10))
plt.yticks(np.arange(7.85, 8.10, 0.01))

# 2
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.pop_x, data.y_poplen2, marker="o", color="orange")

plt.title("Population Size Graph 2")
plt.ylabel("Path Length (meter)")
plt.xlabel("Population Size")

plt.grid(linestyle="--")
plt.legend(["Test 2"], loc="upper right")
plt.xticks(np.arange(0, 200, 10))
plt.yticks(np.arange(7.85, 8.10, 0.01))

# 3
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.pop_x, data.y_poplen3, marker="o", color="green")

plt.title("Population Size Graph 3")
plt.ylabel("Path Length (meter)")
plt.xlabel("Population Size")

plt.grid(linestyle="--")
plt.legend(["Test 3"], loc="upper right")
plt.xticks(np.arange(0, 200, 10))
plt.yticks(np.arange(7.85, 8.5, 0.05))

plt.show() """
