import numpy as np


def h(a, b):
    return b - a


def calculateIntegral(f, segment, step):
    segments = [round(i, 10) for i in np.arange(segment[0], segment[-1] + step / 2., step)]

    sum = 0.0
    for i in range(len(segments) - 1):
        dh = h(segments[i], segments[i + 1])
        sum += f(segments[i] + dh / 2.0) * dh
    return sum
