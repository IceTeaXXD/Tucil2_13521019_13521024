import matplotlib.pyplot as plt

# Plot given points in blue and the closest pair colored in red and draw a line between them in 3D
def result_plot(points, closest_pair):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(*zip(*points))
    ax.scatter(*closest_pair[0], color='red')
    ax.scatter(*closest_pair[1], color='red')
    ax.plot([closest_pair[0][0], closest_pair[1][0]], [closest_pair[0][1], closest_pair[1][1]], [closest_pair[0][2], closest_pair[1][2]], color='red')
    plt.show()
