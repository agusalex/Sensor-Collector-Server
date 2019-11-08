import unittest

from src.models.point import *


class TestStringMethods(unittest.TestCase):

    def test_distance(self):
        d = Point(0, 8).distance(Point(3, 4))
        print(d)
        self.assertEqual(d, 5)

    def test_shift(self):
        p1 = Point(0, 1)
        p1.shift(0, -1)
        self.assertEqual(p1, Point(0, 0))

    def test_find_weighted_midpoint(self):
        p1 = Point(1, 1)
        p2 = Point(4, 2)
        self.assertEqual(Point(2.5, 1.5), p1.find_weighted_midpoint(p2, 1, 1))
        self.assertEqual(Point(3.0000000000000004, 1.6666666666666667), p1.find_weighted_midpoint(p2, 3, 9))
        self.assertEqual(Point(2.0, 1.3333333333333335), p1.find_weighted_midpoint(p2, 9, 3))

    def test_find_proportion(self):
        self.assertEqual(0.8, find_proportion(4, 5))
        self.assertEqual(0.8, find_proportion(5, 4))
        self.assertAlmostEqual(0.75, find_proportion(0.60, 0.80))
        print(find_proportion(0.54, 0.80))


if __name__ == '__main__':
    unittest.main()
