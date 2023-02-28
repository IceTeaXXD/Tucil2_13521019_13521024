import numpy as np
import math

euclidCounter = 0
def EuclideanDistance(point1, point2):
    global euclidCounter
    euclidCounter += 1
    return math.sqrt(sum([(point1[i] - point2[i]) ** 2 for i in range(len(point1))]))