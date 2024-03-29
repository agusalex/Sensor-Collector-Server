import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from random import seed
from random import randint
# use ggplot style for more sophisticated visuals
from src.models.circle import Circle
from src.models.point import Point
from src.least_squares import *


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


def create_circle(circle: Circle, target=False):
    color = matplotlib.cm.jet(randint(50, 100))
    if target:
        color = matplotlib.cm.jet(1000)
    add_shape(plt.Circle((circle.center.x, circle.center.y), color=color, fill=False, zorder=1, radius=circle.radius,
                         alpha=0.8))
    plt.scatter(circle.center.x, circle.center.y, color=color, s=100, zorder=2)


def create_point(point: Point, color=matplotlib.cm.jet(randint(0, 00))):
    plt.scatter(point.x, point.y, color=color, s=100, zorder=2)


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
        circlea = Circle(Point(x, y), 0.5)
        circleb = Circle(Point(x + 0.25, y + 0.25), 0.5)
        drawlist.append(circlea)
        drawlist.append(circleb)
    for intersection in find_intersections(drawlist):
        drawlist.append(intersection)
    draw(drawlist)


def rssiToDistance(rssi):
    return 10 ** (-1 * (rssi + 17) / 38)


def testDraw2():
    # 1
    c1 = Circle(Point(150, 100), rssiToDistance(-72.5948))
    # 3
    c2 = Circle(Point(100, 50), rssiToDistance(-73.2301))
    # 6
    c3 = Circle(Point(76.5, 100), rssiToDistance(-73.3082))

    drawlist = [c1, c2, c3]
    create_circle(leastSquares(drawlist), target=True)
    draw(drawlist)


if __name__ == '__main__':
    testDraw2()
    # testDraw()
