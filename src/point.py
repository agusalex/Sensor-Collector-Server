from math import hypot


class Point:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Point):
            return (self.x == other.x) & (self.y == other.y)
        return False

    def shift(self, x, y):
        self.x += x
        self.y += y


def distance(a, b):
    return hypot(a.x - b.x, a.y - b.y)
