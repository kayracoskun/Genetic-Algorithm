
from config import Config
import matplotlib.pyplot as plt


def show_plot(best_chromosome, inf_time=False):

    plt.figure(num=1)
    plt.clf()
    plt.axis([Config.plt_ax_x_min, Config.plt_ax_x_max, Config.plt_ax_y_min,
              Config.plt_ax_y_max])

    _draw_path_points()
    _draw_obstacles()

    best_path_x = []
    best_path_y = []

    plt.annotate('Start Point', xy=(Config.path_points[int(best_chromosome[0])][0]
                                    + Config.plt_tolerance, Config.path_points[int(best_chromosome[0])][1]))
    plt.annotate('Goal Point', xy=(Config.path_points[int(best_chromosome[-1])][0]
                                   + Config.plt_tolerance, Config.path_points[int(best_chromosome[-1])][1]))

    plt.text(x=Config.plt_ax_x_min, y=Config.plt_ax_y_max + Config.plt_tolerance,
             s='Generation:(%s)' % (Config.generations))

    for element in best_chromosome:

        best_path_x.append(Config.path_points[int(element)][0])
        best_path_y.append(Config.path_points[int(element)][1])

    plt.plot(best_path_x, best_path_y, "g-")
    plt.draw()
    Config.img_iter_no += 1
    if not inf_time:
        plt.pause(0.01)
    else:
        plt.show()


def _draw_path_points():

    node_x = []
    node_y = []

    for element in Config.path_points:
        node_x.append(element[0])
        node_y.append(element[1])

    plt.plot(node_x, node_y, "ko")


def _draw_obstacles():

    obs_1_x = [1.40, 1.73, 1.73, 1.40, 1.40]
    obs_1_y = [7.00, 7.00, 7.60, 7.60, 7.00]
    plt.fill(obs_1_x, obs_1_y, "r")

    plt.legend(('Path points', 'Obstacles'), loc='upper right', fontsize='small',
               numpoints=1, markerscale=0.5, labelspacing=1)

    obs_2_x = [3.37, 3.70, 3.70, 3.37, 3.37]
    obs_2_y = [7.00, 7.00, 7.60, 7.60, 7.00]
    plt.fill(obs_2_x, obs_2_y, "r")

    obs_3_x = [1.70, 2.03, 2.03, 1.70, 1.70]
    obs_3_y = [4.90, 4.90, 4.30, 4.30, 4.90]
    plt.fill(obs_3_x, obs_3_y, "r")

    obs_4_x = [3.00, 5.00, 5.00, 3.00, 3.00]
    obs_4_y = [2.00, 2.00, 4.00, 4.00, 2.00]
    plt.fill(obs_4_x, obs_4_y, "r")

    obs_5_x = [2.80, 5.00, 5.00, 2.80, 2.80]
    obs_5_y = [0, 0, 2.00, 2.00, 0]
    plt.fill(obs_5_x, obs_5_y, "r")
