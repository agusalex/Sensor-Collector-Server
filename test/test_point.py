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


if __name__ == '__main__':
    unittest.main()
