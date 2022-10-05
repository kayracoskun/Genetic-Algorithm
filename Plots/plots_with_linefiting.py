import data
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
plt.rcParams["font.family"] = "Times New Roman"


def lineer_objective(x, a, b):
    return a * x + b


def poly2_objective(x, a, b, c):
    return (a * x) + (b * x**2) + c


def poly3_objective(x, a, b, c, d):
    return (a * x) + (b * x**2) + (c * x**3) + d


def poly4_objective(x, a, b, c, d, e):
    return (a * x) + (b * x**2) + (c * x**3) + (d * x**4) + e


def poly5_objective(x, a, b, c, d, e, f):
    return (a * x) + (b * x**2) + (c * x**3) + (d * x**4) + (e * x**5) + f


""" POPULATION SIZE """
pop_time_av = np.zeros(np.shape(data.pop_x))
pop_len_av = np.zeros(np.shape(data.pop_x))

for i in range(len(pop_time_av)):
    pop_time_av[i] = (data.y_poptime1[i] +
                      data.y_poptime2[i] + data.y_poptime3[i]) / 3

for i in range(len(pop_len_av)):
    pop_len_av[i] = (data.y_poplen1[i] +
                     data.y_poplen2[i] + data.y_poplen3[i]) / 3

pop_time_func, _ = curve_fit(poly3_objective, data.pop_x, pop_time_av)
a1, b1, c1, d1 = pop_time_func
x_line_pt = np.arange(10, 200, 10)
y_line_pt = poly3_objective(x_line_pt, a1, b1, c1, d1)

# Population size plots
# Time Plot
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(x_line_pt, y_line_pt, color="r")
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

pop_len_func, _ = curve_fit(poly4_objective, data.pop_x, pop_len_av)
a2, b2, c2, d2, e2 = pop_len_func
x_line_pl = np.arange(10, 200, 10)
y_line_pl = poly4_objective(x_line_pl, a2, b2, c2, d2, e2)

plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(x_line_pl, y_line_pl, color="r")
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

chr_time_func, _ = curve_fit(poly5_objective, data.chr_x, chr_time_av)
a3, b3, c3, d3, e3, f3 = chr_time_func
x_line_ct = np.arange(9, 16, 1)
y_line_ct = poly5_objective(x_line_ct, a3, b3, c3, d3, e3, f3)

# Chromosome length plots
# Time plots
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(x_line_ct, y_line_ct, color="r")
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

stop_time_func, _ = curve_fit(poly4_objective, data.st_x, st_time_av)
a4, b4, c4, d4, e4 = stop_time_func
x_line_st = np.arange(2, 7, 1)
y_line_st = poly4_objective(x_line_st, a4, b4, c4, d4, e4)

# Stop criterion line plots
# Time plots
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(x_line_st, y_line_st, color="r")
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

mut_time_func, _ = curve_fit(poly5_objective, data.mut_x, mut_time_av)
a5, b5, c5, d5, e5, f5 = mut_time_func
x_line_mt = data.mut_x
y_line_mt = poly5_objective(x_line_mt, a5, b5, c5, d5, e5, f5)

# Mutation rate plots
# Time Plot
plt.figure(figsize=(9.6, 7.2), dpi=120)
plt.plot(x_line_mt, y_line_mt, color="r")
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
