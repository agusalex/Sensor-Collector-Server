from src.point import distance


class Circle:
    def __init__(self, point_init, r_init):
        self.point = point_init
        self.r = r_init

    def __repr__(self):
        return "".join(["Circle(", str(self.point.x), ", ", str(self.point.y), ", ", str(self.r), ")"])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Circle):
            return (self.point.x == other.point.x) & (self.point.y == other.point.y) & (self.r == other.r)
        return False


def intersects(a, b):
    if distance(a.point, b.point) > (a.r + b.r):
        return False  # They dont intersect
    elif distance(a.point, b.point) < abs(a.r - b.r):
        return False  # One is inside the other
    elif (distance(a, b) == 0) and (a.r == b.r):
        return False  # They are exactly the same circle
    else:
        return True


def getIntersectionPoints(a, b):
    ret = []
    return ret
# if intersects(a, b):
