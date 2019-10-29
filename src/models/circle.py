from src.models.point import Point
from math import sqrt
from sqlalchemy import Column, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.db_utils.base import Base


class Circle(Base):
    __tablename__ = 'circle'

    id = Column(Integer, primary_key=True)
    center_id = Column(Integer, ForeignKey("point.id"))
    center = relationship("Point", foreign_keys=[center_id])
    radius = Column(Float)

    def __init__(self, point_init, r_init):
        self.center = point_init
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

    def get_trilateration(self, a, b):
        #TODO:despues sacarlo y que nosea un metodo de clase
        self_a_intersec = self.get_intersection_points(a)
        self_b_intersec = self.get_intersection_points(b)
        a_b_intersec = a.get_intersection_points(b)

        triangle_points = [b.center.closest_point(self_a_intersec), a.center.closest_point(self_b_intersec), self.center.closest_point(a_b_intersec)]

        # coordinate of the vertices
        x1, x2, x3 = triangle_points[0].x, triangle_points[1].x, triangle_points[2].x
        y1, y2, y3 = triangle_points[0].y, triangle_points[1].y, triangle_points[2].y

        # Formula to calculate centroid
        # Despues fijarse si queremos redondear
        # x = round((x1 + x2 + x3) / 3, 2)
        # y = round((y1 + y2 + y3) / 3, 2)

        return Point((x1 + x2 + x3) / 3, (y1 + y2 + y3) / 3)

    #def get_trilateration_2_electric_boogaloo(self, a, b):
        #TODO:despues sacarlo y que nosea un metodo de clase
        #self_a_center_distance = self.center.distance(a.center)
        #self_b_center_distance = self.center.distance(b.center)
        #a_b_center_distance = a.center.distance(b.center)


