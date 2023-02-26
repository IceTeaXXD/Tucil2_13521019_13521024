import numpy as np
from Euclidean import*

def closest_pair(points):
    n = len(points)
    if n <= 1:
        return None, None, float('inf')
    elif n == 2:
        return points[0], points[1], EuclideanDistance(points[0], points[1])
    else:
        sorted_x = sorted(points, key=lambda p: p[0])
        mid = n // 2
        left_x = sorted_x[:mid]
        right_x = sorted_x[mid:]

        left_min_pair = closest_pair(left_x)
        right_min_pair = closest_pair(right_x)
        min_pair = left_min_pair if left_min_pair[2] < right_min_pair[2] else right_min_pair

        mid_x = sorted_x[mid][0]
        strip = []
        for point in points:
            if abs(point[0] - mid_x) < min_pair[2]:
                strip.append(point)

        strip_min_pair = closest_pair_strip(strip, min_pair[2])
        return strip_min_pair if strip_min_pair[2] < min_pair[2] else min_pair

def closest_pair_strip(strip, d):
    min_pair = None, None, d
    sorted_y = sorted(strip, key=lambda p: p[1])
    n = len(sorted_y)
    for i in range(n):
        for j in range(i+1, n):
            if abs(sorted_y[j][1] - sorted_y[i][1]) >= d:
                break
            if EuclideanDistance(sorted_y[i], sorted_y[j]) < min_pair[2]:
                min_pair = sorted_y[i], sorted_y[j], EuclideanDistance(sorted_y[i], sorted_y[j])
    return min_pair

def brute_force(points):
    min = None, None, 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if min[2] == 0:
                min = points[i], points[j], EuclideanDistance(points[i], points[j])
            else:
                if min[2] > EuclideanDistance(points[i], points[j]):
                    min = points[i], points[j], EuclideanDistance(points[i], points[j])
    return min