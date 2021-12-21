import numpy as np

coeff = [
    [1., 1.],
    [1., 4., 1.],
    [1., 3., 3., 1.],
    [7., 32., 12., 32., 7],
    [19., 75., 50., 50., 75., 19.],
    [41., 216., 27., 272., 27., 216., 41.]]

c = [1. / 2., 1. / 3., 3. / 8., 2. / 45., 5. / 288., 1. / 140.]


def h(a, b):
    return b - a


def calculateIntegralSegment(f, segment, n):
    dh = h(segment[0], segment[-1]) / n
    points = [round(i, 10) for i in np.arange(segment[0], segment[-1], dh)]
    if points[-1] != segment[-1]:
        points.append(segment[-1])

    sum = 0
    for i in range(len(points)):
        sum += coeff[n - 1][i] * f(points[i])

    return c[n - 1] * dh * sum


def calculateIntegral(f, segment, step, k):
    points = [round(i, 10) for i in np.arange(segment[0], segment[-1] + step / 2., step)]
    sum = 0.0
    for i in range(len(points) - 1):
        sum += calculateIntegralSegment(f, [points[i], points[i + 1]], k)
    return sum
