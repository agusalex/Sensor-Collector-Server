import unittest

from src.point import *


class TestStringMethods(unittest.TestCase):

    def test_distance(self):
        d = distance(Point(0, 1), Point(2, 3))
        self.assertEqual(d, 2.8284271247461903)

    def test_shift(self):
        p1 = Point(0, 1)
        p1.shift(0, -1)
        self.assertEqual(p1, Point(0, 0))


if __name__ == '__main__':
    unittest.main()
