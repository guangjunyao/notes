#!/bin/python
"""
In geometry, the Fermat point of a triangle, also called the Torricelli point or Fermat–Torricelli point, is a point such that the total distance from the three vertices of the triangle to the point is the minimum possible.
"""
import numpy as np
import matplotlib.pyplot as plt
import math
from functools import reduce


def intersection(c1, c2):
    """find intersection coordinates of two cycles
    c1: cycle1 [x_1, y_1, radius_1]
    c2: cycle1 [x_2, y_2, radius_1]
    """

    x_1 = c1[0]
    y_1 = c1[1]
    R_1 = c1[2]
    x_2 = c2[0]
    y_2 = c2[1]
    R_2 = c2[2]
    d = math.sqrt((abs(x_2-x_1))**2 + (abs(y_2-y_1))**2)
    if d > (R_1+R_2) or d < (abs(R_1-R_2)):
        print("Two circles have no intersection")
        return None
    elif d == 0 and R_1 == R_2:
        print("Two circles have same center!")
        return None
    else:
        A = (R_1**2 - R_2**2 + d**2) / (2 * d)
        h = math.sqrt(R_1**2 - A**2)
        x2 = x_1 + A * (x_2-x_1)/d
        y2 = y_1 + A * (y_2-y_1)/d
        x3 = round(x2 - h * (y_2 - y_1) / d, 2)
        y3 = round(y2 + h * (x_2 - x_1) / d, 2)
        x4 = round(x2 + h * (y_2 - y_1) / d, 2)
        y4 = round(y2 - h * (x_2 - x_1) / d, 2)
        print(x3, y3)
        print(x4, y4)
        i1 = np.array([x3, y3])
        i2 = np.array([x4, y4])
        return np.array([i1, i2])


def find_circumscribing_circle(x_1, y_1, x_2, y_2, x_new, y_new):
    """find a circle from 3 points"""
    a1 = 2 * (x_2 - x_1)
    b1 = 2 * (y_2 - y_1)
    c1 = np.power(x_2, 2) + np.power(y_2, 2) - \
        np.power(x_1, 2) - np.power(y_1, 2)
    a2 = 2 * (x_new - x_2)
    b2 = 2 * (y_new - y_2)
    c2 = np.power(x_new, 2) + np.power(y_new, 2) - \
        np.power(x_2, 2) - np.power(y_2, 2)
    center_x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
    center_y = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1)
    radius = np.sqrt(np.power(x_1 - x_2, 2) +
                     np.power(y_1 - y_2, 2)) / np.sqrt(3)
    return (center_x, center_y, radius)


def find_equilateral_triangles(x_1, y_1, x_2, y_2, x_3, y_3, a):
    """已知三点，求出任意两点组成的等边三角形"""
    angle = np.deg2rad(60)
    if a == 1:
        x_new = x_2 + np.cos(angle) * (x_3 - x_2) + np.sin(angle) * (y_3 - y_2)
        y_new = y_2 - np.sin(angle) * (x_3 - x_2) + np.cos(angle) * (y_3 - y_2)
        check = ((y_2 - y_3) * (x_1 - x_2) + (x_3 - x_2) * (y_1 - y_2)) * (
            (y_2 - y_3) * (x_new - x_2) + (x_3 - x_2) * (y_new - y_2))
        print(check)
        if not check < 0:
            angle = np.deg2rad(-60)
            x_new = x_2 + np.cos(angle) * (x_3 - x_2) + \
                np.sin(angle) * (y_3 - y_2)
            y_new = y_2 - np.sin(angle) * (x_3 - x_2) + \
                np.cos(angle) * (y_3 - y_2)
    elif a == 2:
        x_new = x_1 + np.cos(angle) * (x_3 - x_1) + np.sin(angle) * (y_3 - y_1)
        y_new = y_1 - np.sin(angle) * (x_3 - x_1) + np.cos(angle) * (y_3 - y_1)
        check = ((y_3 - y_1) * (x_2 - x_3) + (x_1 - x_3) * (y_2 - y_3)) * (
            (y_3 - y_1) * (x_new - x_3) + (x_1 - x_3) * (y_new - y_3))
        print(check)
        if not check < 0:
            angle = np.deg2rad(-60)
            x_new = x_1 + np.cos(angle) * (x_3 - x_1) + \
                np.sin(angle) * (y_3 - y_1)
            y_new = y_1 - np.sin(angle) * (x_3 - x_1) + \
                np.cos(angle) * (y_3 - y_1)
    else:
        x_new = x_2 + np.cos(angle) * (x_1 - x_2) + \
            np.sin(angle) * (y_1 - y_2)
        y_new = y_2 - np.sin(angle) * (x_1 - x_2) + np.cos(angle) * (y_1 - y_2)
        check = ((y_2 - y_1) * (x_3 - x_2) + (x_1 - x_2) * (y_3 - y_2)) * (
            (y_2 - y_1) * (x_new - x_2) + (x_1 - x_2) * (y_new - y_2))
        print(check)
        if not check < 0:
            angle = np.deg2rad(-60)
            x_new = x_2 + np.cos(angle) * (x_1 - x_2) + \
                np.sin(angle) * (y_1 - y_2)
            y_new = y_2 - np.sin(angle) * (x_1 - x_2) + \
                np.cos(angle) * (y_1 - y_2)
    return x_new, y_new


def main(x_1, y_1, x_2, y_2, x_3, y_3):
    """先求出任意两点的等边三角形，再画圆"""
    x_new, y_new = find_equilateral_triangles(x_1, y_1, x_2, y_2, x_3, y_3, 1)
    c1 = find_circumscribing_circle(x_2, y_2, x_3, y_3, x_new, y_new)
    x_new, y_new = find_equilateral_triangles(x_1, y_1, x_2, y_2, x_3, y_3, 2)
    c2 = find_circumscribing_circle(x_1, y_1, x_3, y_3, x_new, y_new)
    x_new, y_new = find_equilateral_triangles(x_1, y_1, x_2, y_2, x_3, y_3, 3)
    c3 = find_circumscribing_circle(x_2, y_2, x_1, y_1, x_new, y_new)
    intersection_1 = intersection(c1, c2)
    intersection_2 = intersection(c2, c3)
    intersection_3 = intersection(c1, c3)
    fermat_point = reduce(
        np.intersect1d, ([intersection_1, intersection_2, intersection_3]))
    return fermat_point


if __name__ == '__main__':
    main(2, 5, 5, 5, 6, 7)
