import unittest

from src.circle import *


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
        expected = {Point(1.5, 4.76970), Point(1.5, -4.76970)}# reverse test
        self.assertEqual(c1.get_intersection_points(c2, 5), expected)


if __name__ == '__main__':
    unittest.main()
