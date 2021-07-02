from scipy.optimize import least_squares
from src.graph import *
from src.models.circle import *


def rssiToDistance(rssi):
    return 10 ** (-1 * (rssi + 17) / 38)


def leastSquares(crls, guess=(0, 0, 0)):
    xf, yf, rf = least_squares(equations, guess, args=[crls]).x
    return Circle(Point(xf, yf), rf)


def equations(guess, crls: [Circle]):
    eqs = []
    x, y, r = guess
    for circle in crls:
        eqs.append(((x - circle.center.x) ** 2 + (y - circle.center.y) ** 2 - (circle.radius - r) ** 2))
    return eqs


if __name__ == '__main__':
    circles = [Circle(Point(0, 0, ), rssiToDistance(-72.5958)),
               Circle(Point(16.5, 0), rssiToDistance(-73.3073)),
               Circle(Point(33, 0), rssiToDistance(-73.2301)),
               Circle(Point(50, 0), rssiToDistance(-77.1108)),
               Circle(Point(0, 50), rssiToDistance(-77.1108)),
               Circle(Point(16.5, 50), rssiToDistance(-73.3082)),
               Circle(Point(33, 50), rssiToDistance(-73.231)),
               Circle(Point(50, 50), rssiToDistance(-77.1113)),
               Circle(Point(0, 25), rssiToDistance(-72.5948)),
               Circle(Point(50, 25), rssiToDistance(-72.5948))]
    create_circle(leastSquares(circles), target=True)
    draw([circles[0], circles[1], circles[2], circles[3], circles[4], circles[5], circles[6], circles[7],
          circles[8], circles[9]])

