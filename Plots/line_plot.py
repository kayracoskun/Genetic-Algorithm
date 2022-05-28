from matplotlib import pyplot as plt
import numpy as np
import data

# Population size plots

# Time Plot
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.subplot(2, 1, 1)
plt.plot(data.pop_x, data.y_time1, data.pop_x,
         data.y_time2, data.pop_x, data.y_time3, marker="o")

plt.title("Population Size Graph")
#plt.xlabel("Population Size")
plt.ylabel("Computation Time (second)")

plt.grid(linestyle="--")
plt.legend(["Test 1", "Test 2", "Test 3"], loc="lower right")
plt.xticks(np.arange(0, 200, 10))
plt.yticks(np.arange(0, 0.12, 0.01))

# Length Plot
plt.subplot(2, 1, 2)
plt.plot(data.pop_x, data.y_length1, data.pop_x,
         data.y_length2, data.pop_x, data.y_length3, marker="o")

plt.xlabel("Population Size")
plt.ylabel("Path Length (meter)")

plt.grid(linestyle="--")
plt.legend(["Test 1", "Test 2", "Test 3"], loc="lower right")
plt.xticks(np.arange(0, 200, 10))

plt.show()
