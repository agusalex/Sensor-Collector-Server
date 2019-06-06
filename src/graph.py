import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# use ggplot style for more sophisticated visuals
from src.circle import Circle
from src.point import Point


def live_plotter(x_vec, y1_data, line1, identifier='', pause_time=0.1):
    if line1 == []:
        # this is the call to matplotlib that allows dynamic plotting
        plt.ion()
        fig = plt.figure(figsize=(13, 6))
        ax = fig.add_subplot(111)
        # create a variable for the line so we can later update it
        line1, = ax.plot(x_vec, y1_data, '-o', alpha=0.8)
        # update plot label/title
        plt.ylabel('Y Label')
        plt.title('Title: {}'.format(identifier))
        plt.show()

    # after the figure, axis, and line are created, we only need to update the y-data
    line1.set_ydata(y1_data)
    # adjust limits if new data goes beyond bounds
    if np.min(y1_data) <= line1.axes.get_ylim()[0] or np.max(y1_data) >= line1.axes.get_ylim()[1]:
        plt.ylim([np.min(y1_data) - np.std(y1_data), np.max(y1_data) + np.std(y1_data)])
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    plt.pause(pause_time)

    # return line so we can update it again in the next iteration
    return line1


# the function below is for updating both x and y values (great for updating dates on the x-axis)
def live_plotter_xy(x_vec, y1_data, line1, identifier='', pause_time=0.01):
    if line1 == []:
        plt.ion()
        fig = plt.figure(figsize=(13, 6))
        ax = fig.add_subplot(111)
        line1, = ax.plot(x_vec, y1_data, 'r-o', alpha=0.8)
        plt.ylabel('Y Label')
        plt.title('Title: {}'.format(identifier))
        plt.show()

    line1.set_data(x_vec, y1_data)
    plt.xlim(np.min(x_vec), np.max(x_vec))
    if np.min(y1_data) <= line1.axes.get_ylim()[0] or np.max(y1_data) >= line1.axes.get_ylim()[1]:
        plt.ylim([np.min(y1_data) - np.std(y1_data), np.max(y1_data) + np.std(y1_data)])

    plt.pause(pause_time)

    return line1


def demolive():
    plt.style.use('ggplot')
    size = 100
    x_vec = np.linspace(0, 1, size + 1)[0:-1]
    y_vec = np.random.randn(len(x_vec))
    line1 = []
    while True:
        rand_val = np.random.randn(1)
        y_vec[-1] = rand_val
        line1 = live_plotter(x_vec, y_vec, line1)
        y_vec = np.append(y_vec[1:], 0.0)


def create_circle(circle: Circle):
    color = matplotlib.cm.jet(circle.center.x / 3)  # get the right map, and get the color from the map
    circle = plt.Circle((circle.center.x, circle.center.y), color=color, radius=circle.radius, alpha=0.8)
    add_shape(circle)
    return circle


def create_point(point: Point):
    color = matplotlib.cm.jet(point.x / 3)  # get the right map, and get the color from the map
    point = plt.scatter(point.x, point.y, color=color, s=100)


def add_shape(patch):
    ax = plt.gca()
    ax.add_patch(patch)
    plt.axis('scaled')


def draw(drawlist):
    for item in drawlist:
        if isinstance(item, Circle):
            create_circle(item)
        if isinstance(item, Point):
            create_point(item)
    plt.show()


def find_intersections(list):
    ret = set()
    for item in list:
        for item2 in list:
            if item.intersects(item2):
                for item3 in item.get_intersection_points(item2):
                    print("intersects on " + str(item3))
                    ret.add(item3)
    return ret


def testDraw():
    drawlist = []
    pos = 2.999 * np.random.rand(10, 2)
    for x, y in pos:
        circlea = Circle(x, y, 0.5)
        circleb = Circle(x + 0.25, y + 0.25, 0.5)
        drawlist.append(circlea)
        drawlist.append(circleb)
    for intersection in find_intersections(drawlist):
        drawlist.append(intersection)
    draw(drawlist)


# plt.imsave('demo')


if __name__ == '__main__':
    testDraw()