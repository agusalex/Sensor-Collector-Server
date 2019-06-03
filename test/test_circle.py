import unittest

from src.circle import *


class TestStringMethods(unittest.TestCase):

    def test_shift(self):
        n1 = Circle(0, 1, 10)
        n1.shift(0, -1)
        self.assertEqual(n1.center, Point(0, 0))

    def test_shift_radius(self):
        n1 = Circle(0, 1, 10)
        n2 = Circle(0, 1, 10)
        n1.shift_radius(10)
        n2.shift_radius(-20)
        self.assertEqual(n1.radius, 20)
        self.assertEqual(n2.radius, -10)

    def test_in_radius(self):
        n1 = Circle(0, 0, 10)
        p1 = Point(1, 1)
        p2 = Point(10, 10)
        self.assertTrue(n1.has_inside(p1))
        self.assertFalse(n1.has_inside(p2))


if __name__ == '__main__':
    unittest.main()
