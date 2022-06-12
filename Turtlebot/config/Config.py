import math as ma
import numpy as np

path_points = [[0, 0], [0.2, 0], [0.4, 0], [0.6, 0], [0.8, 0], [1, 0], [1.2, 0], [0, 0.2], [0.4, 0.2], [0.6, 0.2], [0.8, 0.2], [1.2, 0.2], [0, 0.4], [0.2, 0.4], [0.4, 0.4], [0.6, 0.4], [0.8, 0.4], [1, 0.4], [1.2, 0.4], [0, 0.6], [0.2, 0.6], [0.4, 0.6], [
    0.8, 0.6], [1, 0.6], [1.2, 0.6], [0, 0.8], [0.4, 0.8], [0.6, 0.8], [0.8, 0.8], [1.2, 0.8], [0, 1], [0.2, 1], [0.4, 1], [0.6, 1], [0.8, 1], [1, 1], [1.2, 1], [0, 1.2], [0.2, 1.2], [0.4, 1.2], [0.6, 1.2], [0.8, 1.2], [1, 1.2], [1.2, 1.2]]

npts = len(path_points)
pop_max = 1000
mutation_rate = 0.05
start_index = int(0)
end_index = npts - 1
generations = 1
prev_best_fitness = 0
nobs = 9
nbits = ma.log10(npts) / ma.log10(2)
chr_len = int(((nobs+2)*nbits)/nbits)
stop_criteria = 0
stop_generation = False
img_iter_no = 1
plt_tolerance = -1
plt_ax_x_min = -0.1
plt_ax_x_max = 1.3
plt_ax_y_min = -0.1
plt_ax_y_max = 1.4


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

    link = -1 * np.ones((44, 5))

    link[0][0] = 0
    link[0][1] = 7
    link[0][2] = 1

    link[1][0] = 1
    link[1][1] = 2
    link[1][2] = 8

    link[2][0] = 2
    link[2][1] = 8
    link[2][2] = 9
    link[2][3] = 3

    link[3][0] = 3
    link[3][1] = 9
    link[3][2] = 10
    link[3][3] = 4

    link[4][0] = 4
    link[4][1] = 10
    link[4][2] = 5

    link[5][0] = 5
    link[5][1] = 11
    link[5][2] = 6

    link[6][0] = 6
    link[6][1] = 11

    link[7][0] = 7
    link[7][1] = 12
    link[7][2] = 13

    link[8][0] = 8
    link[8][1] = 14
    link[8][2] = 15
    link[8][3] = 19

    link[9][0] = 9
    link[9][1] = 15
    link[9][2] = 16
    link[9][3] = 10

    link[10][0] = 10
    link[10][1] = 16

    link[11][0] = 11
    link[11][1] = 18
    link[11][2] = 17

    link[12][0] = 12
    link[12][1] = 13
    link[12][2] = 19
    link[12][3] = 20

    link[13][0] = 13
    link[13][1] = 14
    link[13][2] = 21
    link[13][3] = 20

    link[14][0] = 14
    link[14][1] = 15
    link[14][2] = 21

    link[15][0] = 15
    link[15][1] = 16
    link[15][2] = 22

    link[16][0] = 16
    link[16][1] = 22
    link[16][2] = 17
    link[16][3] = 23

    link[17][0] = 17
    link[17][1] = 18
    link[17][2] = 24
    link[17][3] = 23

    link[18][0] = 18
    link[18][1] = 24

    link[19][0] = 19
    link[19][1] = 20
    link[19][2] = 25

    link[20][0] = 20
    link[20][1] = 21
    link[20][2] = 26

    link[21][0] = 21
    link[21][1] = 27
    link[21][2] = 26

    link[22][0] = 22
    link[22][1] = 23
    link[22][2] = 28

    link[23][0] = 23
    link[23][1] = 24
    link[23][2] = 29

    link[24][0] = 24
    link[24][1] = 29

    link[25][0] = 25
    link[25][1] = 30
    link[25][2] = 31

    link[26][0] = 26
    link[26][1] = 27
    link[26][2] = 32
    link[26][3] = 33

    link[27][0] = 27
    link[27][1] = 28
    link[27][2] = 34
    link[27][3] = 33

    link[28][0] = 28
    link[28][1] = 34

    link[29][0] = 29
    link[29][1] = 36

    link[30][0] = 30
    link[30][1] = 31
    link[30][2] = 37
    link[30][3] = 38

    link[31][0] = 31
    link[31][1] = 38
    link[31][2] = 39
    link[31][3] = 32

    link[32][0] = 32
    link[32][1] = 33
    link[32][1] = 39
    link[32][1] = 40

    link[33][0] = 33
    link[33][1] = 34
    link[33][2] = 40
    link[33][3] = 41

    link[34][0] = 34
    link[34][1] = 35
    link[34][2] = 41
    link[34][3] = 42

    link[35][0] = 35
    link[35][1] = 36
    link[35][2] = 42
    link[35][2] = 43

    link[36][0] = 36
    link[36][1] = 43

    link[37][0] = 37
    link[37][1] = 38

    link[38][0] = 38
    link[38][1] = 39

    link[39][0] = 39
    link[39][1] = 40

    link[40][0] = 40
    link[40][1] = 41

    link[41][0] = 41
    link[41][1] = 42

    link[42][0] = 42
    link[42][1] = 43

    link[43][0] = 43

    return link
