import numpy as np
import math

euclidCounter = 0
# Calculate Euclidean Distance in R^n
def EuclideanDistance(point1, point2):
    global euclidCounter
    euclidCounter += 1
    return math.sqrt(sum([(point1[i] - point2[i]) ** 2 for i in range(len(point1))]))

def SortPoints(points):
    if len(points) <= 1:
        return points
    else:
        pivot = points[0]
        less = [point for point in points[1:] if point[0] < pivot[0]]
        greater = [point for point in points[1:] if point[0] >= pivot[0]]
        return SortPoints(less) + [pivot] + SortPoints(greater)