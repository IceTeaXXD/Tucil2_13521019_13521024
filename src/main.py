import numpy as np
import matplotlib.pyplot as plt
from ClosestPair import*
from Plot import*

n = int(input("Masukkan banyaknya titik: "))
# generate random points
points = np.random.randint(-100, 100, (n, 3))

min = 0

# brute force method to see closest distance
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        if min == 0:
            min = np.linalg.norm(np.array(points[i]) - np.array(points[j]))
        else:
            if min > np.linalg.norm(np.array(points[i]) - np.array(points[j])):
                min = np.linalg.norm(np.array(points[i]) - np.array(points[j]))

print(min)

closest_pair = closest_pair(points)
print('Closest pair of points:')
print(f'Point 1 : {closest_pair[0]}')
print(f'Point 2 : {closest_pair[1]}')
print(f'Distance: {closest_pair[2]}')
result_plot(points, closest_pair)