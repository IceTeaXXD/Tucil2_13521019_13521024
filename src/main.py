import numpy as np
import matplotlib.pyplot as plt
from ClosestPair import*
from Plot import*

points = [(21, 13, 4), (12, 30, 5), (40, 50, 6), (5, 1, 7), (12, 10, 20), (3, 4, 9)]
closest_pair = closest_pair(points)
print('Closest pair of points:')
print(f'Point 1 : {closest_pair[0]}')
print(f'Point 2 : {closest_pair[1]}')
print(f'Distance: {closest_pair[2]}')
result_plot(points, closest_pair)