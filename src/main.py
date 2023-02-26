import numpy as np
from System import *
from ClosestPair import*
from Plot import*
from time import time
import Euclidean as e

n = int(input("Masukkan banyaknya titik: "))
d = int(input("Masukkan dimensi: "))
points = np.random.randint(-1000, 1000, (n, d))

print("\n== HARDWARE SPECIFICATION ==========----------")
displaySpecification()

start = time()
min = brute_force(points)
end = time()
print(f'Waktu eksekusi brute force: {"{:.2f}".format((end - start) * 1000)} ms')
print(f'Closest distance brute force: {min}')

start = time()
closest_pair = closest_pair(points)
end = time()
print('Closest pair of points:')
print(f'Point 1 : {closest_pair[0]}')
print(f'Point 2 : {closest_pair[1]}')
print(f'Distance: {closest_pair[2]}')
print(f'Waktu eksekusi divide and conquer: {"{:.2f}".format((end - start) * 1000)} ms')
result_plot(points, closest_pair, d)
print(f'Euclidean Distance Total Ops: {e.euclidCounter}')