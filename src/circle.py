from src.point import Point
from math import sqrt


class Circle:
    def __init__(self, x_init, y_init, r_init):
        self.center = Point(x_init, y_init)
        self.radius = r_init

    def __repr__(self):
        return "".join(["Circle(", str(self.center.x), ", ", str(self.center.y), ", ", str(self.radius), ")"])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Circle):
            return (self.center.x == other.center.x) & (self.center.y == other.center.y) & (self.radius == other.radius)
        return False

    def shift(self, x, y):
        self.center.shift(x, y)

    def shift_radius(self, r):
        self.radius += r

    def has_inside(self, point: Point):
        return self.center.distance(point) <= self.radius

    def intersects(self, other):
        if not isinstance(other, Circle):  # if not a circle
            return False
        if self.center.distance(other.center) > (self.radius + other.radius):
            return False  # They dont intersect
        elif self.center.distance(other.center) < abs(self.radius - other.radius):
            return False  # One is inside the other
        elif (self.center.distance(other.center) == 0) and (self.radius == other.radius):
            return False  # They are exactly the same circle
        else:  # if distance(a.center,b.center)<=a.r+b.r
            return True

    def distance_to_intersection(self, other):
        if not isinstance(other, Circle):  # if not a circle
            return None
        return self.center.distance(other.center) - (self.radius + other.radius)

    def get_intersection_points(self, other, precision: int = None):
        if not self.intersects(other):
            return {}

        distance_between_centers = self.center.distance(other.center)
        if precision is not None:
            distance_between_centers = round(distance_between_centers, precision)

        distance_between_x = other.center.x - self.center.x
        distance_between_y = other.center.y - self.center.y
        distance_center_to_middle = (self.radius ** 2 - other.radius ** 2 + distance_between_centers ** 2) / (2 * distance_between_centers)
        distance_between_intersection_points = sqrt(self.radius ** 2 - distance_center_to_middle ** 2)
        intersection_center_x = self.center.x + (distance_center_to_middle * distance_between_x / distance_between_centers)
        intersection_center_y = self.center.y + (distance_center_to_middle * distance_between_y / distance_between_centers)

        intersection_point_a_x = intersection_center_x + (distance_between_intersection_points * distance_between_y) / distance_between_centers
        intersection_point_a_y = intersection_center_y - (distance_between_intersection_points * distance_between_x) / distance_between_centers
        if precision is not None:
            intersection_point_a_x = round(intersection_point_a_x, precision)
            intersection_point_a_y = round(intersection_point_a_y, precision)
        intersection_point_a = Point(intersection_point_a_x, intersection_point_a_y)

        intersection_point_b_x = intersection_center_x - (distance_between_intersection_points * distance_between_y) / distance_between_centers
        intersection_point_b_y = intersection_center_y + (distance_between_intersection_points * distance_between_x) / distance_between_centers
        if precision is not None:
            intersection_point_b_x = round(intersection_point_b_x, precision)
            intersection_point_b_y = round(intersection_point_b_y, precision)
        intersection_point_b = Point(intersection_point_b_x, intersection_point_b_y)

        return {intersection_point_a, intersection_point_b}

