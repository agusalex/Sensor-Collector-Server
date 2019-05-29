import unittest

from src.point import *


class TestStringMethods(unittest.TestCase):

    def test_distance(self):
        d = distance(Point(0, 8), Point(3, 4))
        print(d)
        self.assertEqual(d, 5)

    def test_shift(self):
        p1 = Point(0, 1)
        p1.shift(0, -1)
        self.assertEqual(p1, Point(0, 0))


if __name__ == '__main__':
    unittest.main()
