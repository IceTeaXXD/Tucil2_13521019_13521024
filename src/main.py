import numpy as np
from Splash import *
from System import *
from ClosestPair import*
from Plot import*
from time import time
import Euclidean as e

# Splash Screen
dsiplaySplash()

# Inputs
n = int(input("\nMasukkan banyaknya titik: "))
d = int(input("Masukkan dimensi: "))
points = np.random.randint(-1000, 1000, (n, d))

# Hardware Specification
print("\n== HARDWARE SPECIFICATION ==========----------")
displaySpecification()

# Solution by Brute Force
print("\n== BRUTE FORCE ==========---------------------")
start = time()
min = brute_force(points)
end = time()
print(f'Closest distance: \t{min}')
print(f'Execution time: \t{"{:.2f}".format((end - start) * 1000)} ms')

# Solution by Divide and Conquer
print("\n== DIVIDE AND CONQUER ==========--------------")
start = time()
closest_pair = closest_pair(points)
end = time()
print('Closest pair of points:')
print(f'Point 1 : \t\t{closest_pair[0]}')
print(f'Point 2 : \t\t{closest_pair[1]}')
print(f'Distance: \t\t{closest_pair[2]}')
print(f'Execution time: \t{"{:.2f}".format((end - start) * 1000)} ms')
print(f'Euclidean Distance Total Operations: {e.euclidCounter}')
result_plot(points, closest_pair, d)