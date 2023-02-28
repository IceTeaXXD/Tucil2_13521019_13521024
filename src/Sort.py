def SortPointsByX(points):
    # I.S. points is a list of tuples
    # F.S. returns a list of tuples sorted by the first element (x coordinate) of each tuple
    if len(points) <= 1:
        return points
    else:
        pivot = points[0]
        less = [point for point in points[1:] if point[0] < pivot[0]]
        greater = [point for point in points[1:] if point[0] >= pivot[0]]
        return SortPointsByX(less) + [pivot] + SortPointsByX(greater)
    
def SortPointsByY(points):
    # I.S. points is a list of tuples
    # F.S. returns a list of tuples sorted by the second element (y coordinate) of each tuple
    if len(points) <= 1:
        return points
    else:
        pivot = points[0]
        less = [point for point in points[1:] if point[1] < pivot[1]]
        greater = [point for point in points[1:] if point[1] >= pivot[1]]
        return SortPointsByY(less) + [pivot] + SortPointsByY(greater)