from Euclidean import*
from Sort import*

def closest_pair(points):
    # I.S. points is a list of tuples
    # F.S. returns the tuple consists of point1, point2, and distance
    n = len(points)
    if n <= 1: # Base case (error handling if there is only one point)
        return None, None, float('inf')
    elif n == 2: # Base case
        return points[0], points[1], EuclideanDistance(points[0], points[1])
    else: # Recursive case
        # Divide the points into two halves
        left_x = points[:n//2]
        right_x = points[n//2:]

        # Find the closest pair in each half
        left_min_pair = closest_pair(left_x)
        right_min_pair = closest_pair(right_x)
        min_pair = left_min_pair if left_min_pair[2] < right_min_pair[2] else right_min_pair

        # Find the closest pair that crosses the midpoint (strip)
        mid_x = points[n//2][0]
        strip = []
        for point in points:
            if abs(point[0] - mid_x) < min_pair[2]:
                strip.append(point)

        strip_min_pair = closest_pair_strip(strip, min_pair[2])
        return strip_min_pair if strip_min_pair[2] < min_pair[2] else min_pair

def closest_pair_strip(strip, d):
    # I.S. strip is a list of tuples and d is the distance between the closest pair
    # F.S. returns the tuple consists of point1, point2, and distance
    min_pair = None, None, d
    sorted_y = SortPointsByY(strip)
    n = len(sorted_y)
    # Compare each point with all the points after it (brute force)
    for i in range(n):
        for j in range(i+1, n):
            if abs(sorted_y[j][1] - sorted_y[i][1]) >= d:
                break
            if EuclideanDistance(sorted_y[i], sorted_y[j]) < min_pair[2]:
                min_pair = sorted_y[i], sorted_y[j], EuclideanDistance(sorted_y[i], sorted_y[j])
    return min_pair

def brute_force(points):
    # I.S. points is a list of tuples
    # F.S. returns the tuple consists of point1, point2, and distance
    min = None, None, 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if min[2] == 0: # If min is not initialized
                min = points[i], points[j], EuclideanDistance(points[i], points[j])
            else: 
                if min[2] > EuclideanDistance(points[i], points[j]):
                    min = points[i], points[j], EuclideanDistance(points[i], points[j])
    return min