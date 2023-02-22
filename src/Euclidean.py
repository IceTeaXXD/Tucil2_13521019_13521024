import numpy as np
import math
# Calculate Euclidean Distance in 3D Space
def EuclideanDistance3D(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)

def SortPoints(points):
    for i in range(len(points)):
        min_index = i
        for j in range(i + 1, len(points)):
            if points[j][0] < points[min_index][0]:
                min_index = j
        points[i], points[min_index] = points[min_index], points[i]
    return points