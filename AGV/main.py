#!/usr/bin/env python

"""
Main script

Contains: main function

Author: Yasim Ahmad(yaaximus)

Email: yasim.ahmed63@yahoo.com
"""
from tools.population import population, calculate_distance
from tools.fitness import fitness
from tools.ranking import ranking
from tools.dna import dna
from tools.draw_plot import show_plot

from config import Config
import matplotlib.pyplot as plt

from timeit import default_timer as timer


def main():
    """
    This function encapsulates the cappbilty of initializing chromosome population
    and then continue calculating fitness, generate ranking, perform crossover and
    mutation & repeating above steps until a defined stopping crietia is not met.
    """

    chr_population = population()

    chr_pop_fitness, chr_best_fitness_index = fitness(chr_pop=chr_population)

    chr_ranked_population = ranking(
        chr_pop_fitness=chr_pop_fitness, pop=chr_population)

    chr_crossover_mutated_population = dna(chr_pop_fitness=chr_pop_fitness,
                                           ranked_population=chr_ranked_population, chr_best_fitness_index=chr_best_fitness_index, last_pop=chr_population)

   # show_plot(best_chromosome=chr_crossover_mutated_population[0])

    while not Config.stop_generation:

        prev_best_fit = chr_pop_fitness[chr_best_fitness_index[0], 0]

        chr_pop_fitness, chr_best_fitness_index = fitness(
            chr_pop=chr_crossover_mutated_population)

        chr_ranked_population = ranking(chr_pop_fitness=chr_pop_fitness,
                                        pop=chr_crossover_mutated_population)

        chr_crossover_mutated_population = dna(chr_pop_fitness=chr_pop_fitness,
                                               ranked_population=chr_ranked_population, chr_best_fitness_index=chr_best_fitness_index, last_pop=chr_crossover_mutated_population)

        if prev_best_fit == chr_pop_fitness[chr_best_fitness_index[0], 0]:
            Config.stop_criteria += 1
        else:
            Config.stop_criteria = 0

        if Config.stop_criteria >= 5:
            Config.stop_generation = True
            # plt.close('all')

        print("Best chromosome is:",
              chr_crossover_mutated_population[chr_best_fitness_index[0]])

        # show_plot(best_chromosome=chr_crossover_mutated_population[0])
        Config.generations += 1

    #show_plot(best_chromosome=chr_crossover_mutated_population[0], inf_time=True)
    return chr_crossover_mutated_population[chr_best_fitness_index[0]]


start = timer()
best_chromo = main()
end = timer()
best_chromo_coord = []

for p in best_chromo:
    point = int(p)
    best_chromo_coord.append(Config.path_points[point])

path = 0
for p in range(len(best_chromo_coord)-1):
    path = path + \
        calculate_distance(best_chromo_coord[p], best_chromo_coord[p+1])

print("-"*150)
print("Final: ", best_chromo)
print("Coord: ", best_chromo_coord)
print("\nLength: ", path)
print("Time: ", end-start)
