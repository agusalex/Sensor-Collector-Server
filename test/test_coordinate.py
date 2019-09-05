import unittest

from src.models.coordinate import *


class TestStringMethods(unittest.TestCase):

    def test_shift(self):
        p1 = Coordinate(0, 1)
        p1.shift(0, -1)
        self.assertEqual(p1, Coordinate(0, 0))

    def test_distance(self):
        point_a = Coordinate(52.2296756, 21.0122287)
        point_b = Coordinate(52.406374, 16.9251681)
        self.assertEqual(point_a.distance(point_b), 278.54558935106695)
        ungs = Coordinate(-34.5359069, -58.7153467)
        point_c = Coordinate(-34.5282916, -58.714135)
        self.assertEqual(ungs.distance( point_c), 0.8542944715822927)


if __name__ == '__main__':
    unittest.main()
