import matplotlib.pyplot as plt
import numpy as np


def axisSetUp():
    ax = plt.gca()  # gca stands for 'get current axis'
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))


def build(f, segment):
    axisSetUp()

    x = np.arange(segment[0], segment[-1], 0.1)
    y = [f(x[i]) for i in range(len(x))]
    plt.plot(x, y)

    pointsY = [f(segment[i]) for i in range(len(segment))]
    for i_x, i_y in zip(segment, pointsY):
        plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))

    plt.show()
