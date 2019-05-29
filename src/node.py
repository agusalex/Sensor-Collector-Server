from src.point import Point
from math import hypot


class Node:
    def __init__(self, x_init, y_init, radius_init):
        self.x = x_init
        self.y = y_init
        self.radius = radius_init

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")", " Radius: ", str(self.radius)])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Node):
            return (self.x == other.x) & (self.y == other.y) & (self.radius == other.radius)
        return False

    def shift(self, x, y):
        self.x += x
        self.y += y

    def shift_radius(self, r):
        self.radius += r

    def in_radius(self, point: Point):
        return self.point_distance_to_center(point) <= self.radius

    def point_distance_to_center(self, point: Point):
        return hypot(self.x - point.x, self.y - point.y)

    def node_distance_to_center(self, other):
        if isinstance(other, Node):
            return self.point_distance_to_center(other.get_center()) - other.radius
        return -1

    def get_center(self):
        return Point(self.x, self.y)


def within_range(node_a: Node, node_b: Node):
    return node_a.point_distance_to_center(node_b.get_center()) <= node_a.radius + node_b.radius
