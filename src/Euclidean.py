import numpy as np
import math
# Calculate Euclidean Distance in R^n
def EuclideanDistance3D(point1, point2):
    return math.sqrt(sum([(point1[i] - point2[i]) ** 2 for i in range(len(point1))]))

def SortPoints(points):
    for i in range(len(points)):
        min_index = i
        for j in range(i + 1, len(points)):
            if points[j][0] < points[min_index][0]:
                min_index = j
        points[i], points[min_index] = points[min_index], points[i]
    return points