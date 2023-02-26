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
bf_extime = (end-start) * 1000
bf_euclidop = e.euclidCounter
print('Closest pair of points:')
print(f'Point 1 : \t\t{min[0]}')
print(f'Point 2 : \t\t{min[1]}')
print(f'Distance: \t\t{min[2]}')
print(f'Execution time: \t{"{:.2f}".format(bf_extime)} ms')
print(f'Euclidean Distance Operations: {bf_euclidop}')

# Solution by Divide and Conquer
print("\n== DIVIDE AND CONQUER ==========--------------")
start = time()
closest_pair = closest_pair(points)
end = time()
dc_extime = (end-start) * 1000
dc_euclidop = e.euclidCounter-bf_euclidop
print('Closest pair of points:')
print(f'Point 1 : \t\t{closest_pair[0]}')
print(f'Point 2 : \t\t{closest_pair[1]}')
print(f'Distance: \t\t{closest_pair[2]}')
print(f'Execution time: \t{"{:.2f}".format(dc_extime)} ms')
print(f'Euclidean Distance Operations: {dc_euclidop}')


# Comparison
print("\n== SOLUTIONS COMPARISON ==========-----------")
if(closest_pair[2] == min[2]):
    print("Solutions match")
else:
    print("Solutions does not match")
if(dc_extime < bf_extime):
    print(f"Divide and conquer is faster by {'{:.2f}'.format(bf_extime-dc_extime)} ms")
else:
    print(f"Brute force is faster by {'{:.2f}'.format(dc_extime-dc_extime)} ms")
if(dc_euclidop < bf_euclidop):
    print(f"Divide and conquer used {bf_euclidop-dc_euclidop} less euclidian distance operations")
else:
    print(f"Brute force used {dc_euclidop-bf_euclidop} less euclidian distance operations")
print("\n")

result_plot(points, closest_pair, d)