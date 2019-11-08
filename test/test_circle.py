import unittest

from src.models.circle import *


class TestStringMethods(unittest.TestCase):

    def test_shift(self):
        c1 = Circle(Point(0, 1), 10)
        c1.shift(0, -1)
        self.assertEqual(c1.center, Point(0, 0))

    def test_shift_radius(self):
        c1 = Circle(Point(0, 1), 10)
        c2 = Circle(Point(0, 1), 10)
        c1.shift_radius(10)
        c2.shift_radius(-20)
        self.assertEqual(c1.radius, 20)
        self.assertEqual(c2.radius, -10)

    def test_in_radius(self):
        c1 = Circle(Point(0, 0), 10)
        p1 = Point(1, 1)
        p2 = Point(10, 10)
        self.assertTrue(c1.has_inside(p1))
        self.assertFalse(c1.has_inside(p2))

    def test_get_intersection_points(self):
        c1 = Circle(Point(0, 0), 5)
        c2 = Circle(Point(3, 0), 5)
        expected = {Point(1.5, -4.76970), Point(1.5, 4.76970)}
        self.assertEqual(c1.get_intersection_points(c2, 5), expected)
        expected = {Point(1.5, 4.76970), Point(1.5, -4.76970)}  # reverse test
        self.assertEqual(c1.get_intersection_points(c2, 5), expected)

    def test_proportion(self):
        c1 = Circle(Point(0, 0), 1)
        c2 = Circle(Point(2, 0), 3)
        print(c1.get_proportion(c2))

    def test_trilateration(self):
        c1 = Circle(Point(0, 0), 2)
        c2 = Circle(Point(2, 0), 2)
        c3 = Circle(Point(1, 2), 2)
        self.assertEqual(c1.get_trilateration(c2, c3), Point(1.0, 0.6666666666666666))

    def test_trilateration2(self):
        #Triple Intersection example
        c1 = Circle(Point(0, 0), 2)
        c2 = Circle(Point(2, 0), 2)
        c3 = Circle(Point(1, 2), 2)
        self.assertEqual(c1.get_trilateration2(c2, c3), Point(1.0, 0.6666666666666666))
        #No intersection
        c1 = Circle(Point(0, 0), 0.5)
        c2 = Circle(Point(2, 0), 0.5)
        c3 = Circle(Point(1, 2), 0.5)
        self.assertEqual(c1.get_trilateration2(c2, c3), Point(1.0, 0.6666666666666666))
        #Test Weighted
        c1 = Circle(Point(0, 0), 0.5)
        c2 = Circle(Point(2, 0), 0.5)
        c3 = Circle(Point(1, 2), 0.5)
        self.assertEqual(c1.get_trilateration2(c2, c3), Point(1.0, 0.6666666666666666))



if __name__ == '__main__':
    unittest.main()
