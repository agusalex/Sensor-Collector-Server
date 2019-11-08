from math import hypot

from sqlalchemy import Column, Float, Integer
from src.db_utils.base import Base


class Point(Base):
    __tablename__ = 'point'

    id = Column(Integer, primary_key=True)
    x = Column(Float)
    y = Column(Float)

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

    def __hash__(self):
        return hash(str(self))

    def shift(self, x, y):
        self.x += x
        self.y += y

    def sum(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def substract(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def multiply(self, factor):
        return Point(self.x * factor, self.y * factor)

    def distance(self, b):
        return hypot(self.x - b.x, self.y - b.y)

    def find_weighted_midpoint(self, other, self_weight: float, other_weight: float):
        if self_weight == other_weight:
            midpoint = self.sum(other)
            return midpoint.multiply(0.5)
        proportion = find_proportion(self_weight, other_weight)
        one_minus_p = 1 - proportion
        a = Point(self.x, self.y)
        b = Point(other.x, other.y)

        if self_weight > other_weight:  # if self is bigger one
            a = a.multiply(one_minus_p)
            b = b.multiply(proportion)
        else:
            a = a.multiply(proportion)
            b = b.multiply(one_minus_p)

        return a.sum(b)

    def closest_point(self, array):
        minimum_distance = float('inf')
        minimum_point = None
        for point in array:
            if point.distance(self) < minimum_distance:
                minimum_distance = point.distance(self)
                minimum_point = self
        return minimum_point


def find_proportion(self_weight, other_weight):
    if self_weight == other_weight:
        return 0.5
    bigger = max(self_weight, other_weight)
    smaller = min(self_weight, other_weight)
    return float(smaller) / float(bigger)
