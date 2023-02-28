import matplotlib.pyplot as plt

def result_plot(points, closest_pair, dimension):
    # I.S. points is a list of tuples, closest_pair is a tuple of two tuples, and dimension is an integer
    # F.S. Plot given points in blue and the closest pair colored in red and draw a line between them in given dimension
    if dimension == 2:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(*zip(*points))
        ax.scatter(*closest_pair[0], color='red')
        ax.scatter(*closest_pair[1], color='red')
        ax.plot([closest_pair[0][0], closest_pair[1][0]], [closest_pair[0][1], closest_pair[1][1]], color='red')
        plt.show()

    elif dimension == 3:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(*zip(*points))
        ax.scatter(*closest_pair[0], color='red')
        ax.scatter(*closest_pair[1], color='red')
        ax.plot([closest_pair[0][0], closest_pair[1][0]], [closest_pair[0][1], closest_pair[1][1]], [closest_pair[0][2], closest_pair[1][2]], color='red')
        plt.show()
    
    else:
        print('Plotting is only available in 2D and 3D\n')