from src.point import Point


class Circle:
    def __init__(self, x, y, r_init):
        self.center = Point(x, y)
        self.radius = r_init

    def __repr__(self):
        return "".join(["Circle(", str(self.center.x), ", ", str(self.center.y), ", ", str(self.radius), ")"])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Circle):
            return (self.center.x == other.center.x) & (self.center.y == other.center.y) & (self.radius == other.radius)
        return False

    def shift(self, x, y):
        self.center.x += x
        self.center.y += y

    def shift_radius(self, r):
        self.radius += r

    def has_inside(self, point: Point):
        if self.center.distance(point) <= self.radius:
            return True
        return False

    def intersects(self, other):
        if not isinstance(other, Circle):  # if not a circle
            return False
        if self.center.distance(other.center) > (self.r + other.r):
            return False  # They dont intersect
        elif self.center.distance(other.center) < abs(self.r - other.r):
            return False  # One is inside the other
        elif (self.center.distance(other.center) == 0) and (self.r == other.r):
            return False  # They are exactly the same circle
        else:  # if distance(a.center,b.center)<=a.r+b.r
            return True

    def distance_to_intersection(self, other):
        if not isinstance(other, Circle):  # if not a circle
            return None
        return self.center.distance(other.center) - (self.radius + other.radius)

    def get_intersection_points(self, other):  # Unimplemented

        return None
