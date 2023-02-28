import math

euclidCounter = 0
def EuclideanDistance(point1, point2):
    # I.S. point1 and point2 are tuples of the same length
    # F.S. returns the Euclidean distance between point1 and point2
    global euclidCounter
    euclidCounter += 1
    return math.sqrt(sum([(point1[i] - point2[i]) ** 2 for i in range(len(point1))])) # The formula counts the distance between two points in n-dimensional space