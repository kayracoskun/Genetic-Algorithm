import math as ma
import numpy as np

path_points = [[0.5, 1], [1, 1], [1.5, 1], [2, 1], [0.5, 2], [1, 2], [1.5, 2], [2, 2], [0.5, 3], [1, 3], [1.5, 3], [2, 3], [2.5, 3], [0.5, 4], [1, 4], [2.5, 4], [0.5, 5], [1, 5], [3, 5], [
    3.5, 5], [4, 5], [4.5, 5], [0.5, 6], [1, 6], [1.5, 6], [2, 6], [2.5, 6], [3, 6], [3.5, 6], [4, 6], [4.5, 6], [0.5, 7], [2.5, 7], [4.5, 7], [0.5, 8], [4.5, 8], [2.5, 8]]

npts = len(path_points)
pop_max = 100
mutation_rate = 0.05
start_index = int(0)
end_index = npts - 1
generations = 1
prev_best_fitness = 0
nobs = 8
nbits = ma.log10(npts) / ma.log10(2)
chr_len = int(((nobs+2)*nbits)/nbits)
stop_criteria = 0
stop_generation = False
img_iter_no = 1
plt_tolerance = -0.5
plt_ax_x_min = 0
plt_ax_x_max = 5
plt_ax_y_min = 0
plt_ax_y_max = 9


def define_links():
    """
    This function defines the links b/w path points

    Returns
    -------
    [numpy.ndarray]
        [Every path point has a number of allowed connection with other path 
        points. Those allowed connections are defined below. During calculation
        of fitness of population if two consecutive path points are connected
        then the fitness of that chromosome increases]
    """

    link = -1 * np.ones((37, 5))

    link[0][0] = 0
    link[0][1] = 1
    link[0][2] = 5
    link[0][3] = 4

    link[1][0] = 1
    link[1][1] = 2
    link[1][2] = 6
    link[1][3] = 5
    link[1][4] = 4

    link[2][0] = 2
    link[2][1] = 3
    link[2][2] = 7
    link[2][3] = 6
    link[2][4] = 5

    link[3][0] = 3
    link[3][1] = 7
    link[3][2] = 6

    link[4][0] = 4
    link[4][1] = 5
    link[4][2] = 9
    link[4][3] = 8

    link[5][0] = 5
    link[5][1] = 6
    link[5][2] = 10
    link[5][3] = 9
    link[5][4] = 8

    link[6][0] = 6
    link[6][1] = 7
    link[6][2] = 11
    link[6][3] = 10
    link[6][4] = 9

    link[7][0] = 7
    link[7][1] = 12
    link[7][2] = 11
    link[7][3] = 10

    link[8][0] = 8
    link[8][1] = 9
    link[8][2] = 14
    link[8][3] = 13

    link[9][0] = 9
    link[9][1] = 10
    link[9][2] = 14
    link[9][3] = 13

    link[10][0] = 10
    link[10][1] = 11
    link[10][2] = 14

    link[11][0] = 11
    link[11][1] = 12
    link[11][2] = 15

    link[12][0] = 12
    link[12][1] = 15

    link[13][0] = 13
    link[13][1] = 14
    link[13][2] = 17
    link[13][3] = 16

    link[14][0] = 14
    link[14][1] = 17
    link[14][2] = 16

    link[15][0] = 15
    link[15][1] = 18

    link[16][0] = 16
    link[16][1] = 17
    link[16][2] = 23
    link[16][3] = 22

    link[17][0] = 17
    link[17][1] = 24
    link[17][2] = 23
    link[17][3] = 22

    link[18][0] = 18
    link[18][1] = 19
    link[18][2] = 28
    link[18][3] = 27
    link[18][4] = 26

    link[19][0] = 19
    link[19][1] = 20
    link[19][2] = 29
    link[19][3] = 28
    link[19][4] = 27

    link[20][0] = 20
    link[20][1] = 21
    link[20][2] = 30
    link[20][3] = 29
    link[20][4] = 28

    link[21][0] = 21
    link[21][1] = 30
    link[21][1] = 29

    link[22][0] = 22
    link[22][1] = 23
    link[22][2] = 31

    link[23][0] = 23
    link[23][1] = 24
    link[23][2] = 31

    link[24][0] = 24
    link[24][1] = 25

    link[25][0] = 25
    link[25][1] = 26
    link[25][2] = 32

    link[26][0] = 26
    link[26][1] = 27
    link[26][2] = 32

    link[27][0] = 27
    link[27][1] = 28
    link[27][2] = 32

    link[28][0] = 28
    link[28][1] = 29

    link[29][0] = 29
    link[29][1] = 30
    link[29][2] = 33

    link[30][0] = 30
    link[30][1] = 33

    link[31][0] = 31
    link[31][1] = 34

    link[32][0] = 32
    link[32][1] = 36

    link[33][0] = 33
    link[33][1] = 35

    link[34][0] = 34
    link[34][1] = 36

    link[35][0] = 35
    link[35][1] = 36

    link[36][0] = 36

    return link
