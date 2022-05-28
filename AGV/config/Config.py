import math as ma
import numpy as np

path_points = [[50, 100], [100, 100], [150, 100], [50, 200], [100, 200], [150, 200], [50, 300], [100, 300], [150, 300], [200, 300], [250, 300], [50, 400], [100, 400], [250, 400], [50, 500], [100, 500], [300, 500], [
    350, 500], [400, 500], [450, 500], [50, 600], [100, 600], [150, 600], [200, 600], [250, 600], [300, 600], [350, 600], [400, 600], [450, 600], [50, 700], [250, 700], [450, 700], [50, 800], [450, 800], [250, 800]]

npts = len(path_points)
pop_max = 1000
mutation_rate = 0.005
start_index = int(0)
end_index = npts - 1
generations = 1
prev_best_fitness = 0
nobs = 18
nbits = ma.log10(npts) / ma.log10(2)
chr_len = int(((nobs+2)*nbits)/nbits)
stop_criteria = 0
stop_generation = False
img_iter_no = 1
plt_tolerance = -1
plt_ax_x_min = 0
plt_ax_x_max = 500
plt_ax_y_min = 0
plt_ax_y_max = 900


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

    link = -1 * np.ones((35, 5))

    link[0][0] = 0
    link[0][1] = 1
    link[0][2] = 4
    link[0][3] = 3

    link[1][0] = 1
    link[1][1] = 2
    link[1][2] = 5
    link[1][3] = 4
    link[1][4] = 3

    link[2][0] = 2
    link[2][1] = 5
    link[2][2] = 4

    link[3][0] = 3
    link[3][1] = 4
    link[3][2] = 7
    link[3][3] = 6

    link[4][0] = 4
    link[4][1] = 5
    link[4][2] = 8
    link[4][3] = 7
    link[4][4] = 6

    link[5][0] = 5
    link[5][1] = 9
    link[5][2] = 8
    link[5][3] = 7

    link[6][0] = 6
    link[6][1] = 7
    link[6][2] = 11
    link[6][3] = 12

    link[7][0] = 7
    link[7][1] = 8
    link[7][2] = 12
    link[7][3] = 11

    link[8][0] = 8
    link[8][1] = 9
    link[8][2] = 13
    link[8][3] = 12

    link[9][0] = 9
    link[9][1] = 10
    link[9][2] = 13
    link[9][3] = 12

    link[10][0] = 10
    link[10][1] = 13

    link[11][0] = 11
    link[11][1] = 12
    link[11][2] = 15
    link[11][3] = 14

    link[12][0] = 12
    link[12][1] = 15
    link[12][2] = 14

    link[13][0] = 13
    link[13][1] = 16

    link[14][0] = 14
    link[14][1] = 15
    link[14][2] = 21
    link[14][3] = 20

    link[15][0] = 15
    link[15][1] = 20
    link[15][2] = 21
    link[15][3] = 22

    link[16][0] = 16
    link[16][1] = 17
    link[16][2] = 26
    link[16][3] = 25
    link[16][0] = 24

    link[17][0] = 17
    link[17][1] = 18
    link[17][2] = 27
    link[17][3] = 26
    link[17][4] = 25

    link[18][0] = 18
    link[18][1] = 19
    link[18][2] = 28
    link[18][3] = 27
    link[18][4] = 26

    link[19][0] = 19
    link[19][1] = 28
    link[19][2] = 27

    link[20][0] = 20
    link[20][1] = 21
    link[20][2] = 29

    link[21][0] = 21
    link[21][1] = 22
    link[21][1] = 29

    link[22][0] = 22
    link[22][1] = 23

    link[23][0] = 23
    link[23][1] = 24
    link[23][2] = 30

    link[24][0] = 24
    link[24][1] = 25
    link[24][2] = 30

    link[25][0] = 25
    link[25][1] = 26
    link[25][2] = 30

    link[26][0] = 26
    link[26][1] = 27

    link[27][0] = 27
    link[27][1] = 28
    link[27][2] = 31

    link[28][0] = 28
    link[28][1] = 31

    link[29][0] = 29
    link[29][1] = 32

    link[30][0] = 30
    link[30][1] = 34

    link[31][0] = 31
    link[31][1] = 33

    link[32][0] = 32
    link[32][1] = 34

    link[33][0] = 33
    link[33][1] = 34

    link[34][0] = 34

    return link
