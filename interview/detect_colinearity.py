# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 17:47:27 2018

@author: Wei Wu
"""


def collinear(points):
    """ Calculation the area of
        triangle. We have skipped
        multiplication with 0.5 to
        avoid floating point computations """
    # a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    # a == 0 if three points ly on the same line
    import itertools
    temp = []
    combinations = list(itertools.combinations(points, 3))
    for point in combinations:
        a = point[0][0] * (point[1][1] - point[2][1]) +\
            point[1][0] * (point[2][1] - point[0][1]) + \
            point[2][0] * (point[0][1] - point[1][1])
        if (a == 0):
            temp.append(0)
        else:
            temp.append(1)
        if 1 in temp:
            return 0
        else:
            return 1


# Driver Code
points = [[1, 1], [1, 1], [2, 3], [0, 0]]
print(collinear(points))
