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

""" # Mutation rate line plots
# Time Plot
# 1
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.mut_x, data.y_muttime1, marker="o")

plt.title("Mutation Rate Graph 1")
plt.ylabel("Computation Time (second)")
plt.xlabel("Mutation Rate")

plt.grid(linestyle="--")
plt.legend(["Test 1"], loc="lower right")
plt.xticks(np.arange(0, 0.25, 0.025))
plt.yticks(np.arange(0.042, 0.0505, 0.0005))

# 2
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.mut_x, data.y_muttime2, marker="o", color="orange")

plt.title("Mutation Rate Graph 2")
plt.ylabel("Computation Time (second)")
plt.xlabel("Mutation Rate")

plt.grid(linestyle="--")
plt.legend(["Test 2"], loc="lower right")
plt.xticks(np.arange(0, 0.25, 0.025))
plt.yticks(np.arange(0.043, 0.059, 0.001))

# 3
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.mut_x, data.y_muttime3, marker="o", color="green")

plt.title("Mutation Rate Graph 3")
plt.ylabel("Computation Time (second)")
plt.xlabel("Mutation Rate")

plt.grid(linestyle="--")
plt.legend(["Test 3"], loc="upper right")
plt.xticks(np.arange(0, 0.25, 0.025))
plt.yticks(np.arange(0.043, 0.0515, 0.0005)) """

""" # Length Plot
# 1
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.mut_x, data.y_mutlen1, marker="o")

plt.title("Mutation Rate Graph 1")
plt.ylabel("Path Length (meter)")
plt.xlabel("Mutation Rate")

plt.grid(linestyle="--")
plt.legend(["Test 1"], loc="upper right")
plt.xticks(np.arange(0, 0.25, 0.025))
#plt.yticks(np.arange(7.8, 8, 0.01))

# 2
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.mut_x, data.y_mutlen2, marker="o", color="orange")

plt.title("Mutation Rate Graph 2")
plt.ylabel("Path Length (meter)")
plt.xlabel("Mutation Rate")

plt.grid(linestyle="--")
plt.legend(["Test 2"], loc="upper right")
plt.xticks(np.arange(0, 0.25, 0.025))
#plt.yticks(np.arange(7.8, 8))

# 3
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.mut_x, data.y_mutlen3, marker="o", color="green")

plt.title("Mutation Rate Graph 3")
plt.ylabel("Path Length (meter)")
plt.xlabel("Mutation Rate")

plt.grid(linestyle="--")
plt.legend(["Test 3"], loc="upper right")
plt.xticks(np.arange(0, 0.25, 0.025))
#plt.yticks(np.arange(7.8, 8, 0.005))

plt.show() """

""" # Chromosome length line plots
# Time Plot
# 1
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.chr_x, data.y_chrtime1, marker="o")

plt.title("Chromosome Length Graph 1")
plt.ylabel("Computation Time (second)")
plt.xlabel("Chromosome Length")

plt.grid(linestyle="--")
plt.legend(["Test 1"], loc="lower right")
plt.xticks(np.arange(9, 13, 1))
plt.yticks(np.arange(0.036, 0.051, 0.001))

# 2
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.chr_x, data.y_chrtime2, marker="o", color="orange")

plt.title("Chromosome Length Graph 2")
plt.ylabel("Computation Time (second)")
plt.xlabel("Chromosome Length")

plt.grid(linestyle="--")
plt.legend(["Test 2"], loc="lower right")
plt.xticks(np.arange(9, 13, 1))
plt.yticks(np.arange(0.038, 0.052, 0.001))

# 3
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.chr_x, data.y_chrtime3, marker="o", color="green")

plt.title("Chromosome Length Graph 3")
plt.ylabel("Computation Time (second)")
plt.xlabel("Chromosome Length")

plt.grid(linestyle="--")
plt.legend(["Test 3"], loc="upper right")
plt.xticks(np.arange(9, 13, 1))
plt.yticks(np.arange(0.038, 0.052, 0.001))
plt.show() """

""" # Length Plot
# 1
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.chr_x, data.y_chrlen1, marker="o")

plt.title("Chromosome Length Graph 1")
plt.ylabel("Path Length (meter)")
plt.xlabel("Chromosome Length")

plt.grid(linestyle="--")
plt.legend(["Test 1"], loc="upper right")
plt.xticks(np.arange(9, 14, 1))
#plt.yticks(np.arange(7.8, 8, 0.0001))

# 2
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.chr_x, data.y_chrlen2, marker="o", color="orange")

plt.title("Chromosome Length Graph 2")
plt.ylabel("Path Length (meter)")
plt.xlabel("Chromosome Length")

plt.grid(linestyle="--")
plt.legend(["Test 2"], loc="upper right")
plt.xticks(np.arange(9, 14, 1))
#plt.yticks(np.arange(7.8, 8))

# 3
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.chr_x, data.y_chrlen3, marker="o", color="green")

plt.title("Chromosome Length Graph 3")
plt.ylabel("Path Length (meter)")
plt.xlabel("Chromosome Length")

plt.grid(linestyle="--")
plt.legend(["Test 3"], loc="upper right")
plt.xticks(np.arange(9, 14, 1))
#plt.yticks(np.arange(7.8, 8, 0.005))

plt.show() """

""" # Stop Criteria line plots
# Time Plot
# 1
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.st_x, data.y_sttime1, marker="o")

plt.title("Stop Criteria Graph 1")
plt.ylabel("Computation Time (second)")
plt.xlabel("Stop Criteria")

plt.grid(linestyle="--")
plt.legend(["Test 1"], loc="lower right")
plt.xticks(np.arange(2, 7, 1))
plt.yticks(np.arange(0.03, 0.08, 0.005))

# 2
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.st_x, data.y_sttime2, marker="o", color="orange")

plt.title("Stop Criteria Graph 2")
plt.ylabel("Computation Time (second)")
plt.xlabel("Stop Criteria")

plt.grid(linestyle="--")
plt.legend(["Test 2"], loc="lower right")
plt.xticks(np.arange(2, 7, 1))
plt.yticks(np.arange(0.03, 0.065, 0.0025))

# 3
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.st_x, data.y_sttime3, marker="o", color="green")

plt.title("Stop Criteria Graph 3")
plt.ylabel("Computation Time (second)")
plt.xlabel("Stop Criteria")

plt.grid(linestyle="--")
plt.legend(["Test 3"], loc="lower right")
plt.xticks(np.arange(2, 7, 1))
plt.yticks(np.arange(0.03, 0.08, 0.005))
plt.show() """

# Length Plot
# 1
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.st_x, data.y_stlen1, marker="o")

plt.title("Stop Criteria Graph 1")
plt.ylabel("Path Length (meter)")
plt.xlabel("Stop Criteria")

plt.grid(linestyle="--")
plt.legend(["Test 1"], loc="upper right")
plt.xticks(np.arange(2, 7, 1))
#plt.yticks(np.arange(7.8, 8, 0.0001))

# 2
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.st_x, data.y_stlen2, marker="o", color="orange")

plt.title("Stop Criteria Graph 2")
plt.ylabel("Path Length (meter)")
plt.xlabel("Stop Criteria")

plt.grid(linestyle="--")
plt.legend(["Test 2"], loc="upper right")
plt.xticks(np.arange(2, 7, 1))
#plt.yticks(np.arange(7.8, 8))

# 3
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(data.st_x, data.y_stlen3, marker="o", color="green")

plt.title("Stop Criteria Graph 3")
plt.ylabel("Path Length (meter)")
plt.xlabel("Stop Criteria")

plt.grid(linestyle="--")
plt.legend(["Test 3"], loc="upper right")
plt.xticks(np.arange(2, 7, 1))
#plt.yticks(np.arange(7.8, 8, 0.005))

plt.show()
