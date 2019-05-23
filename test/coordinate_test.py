import unittest

from src.coordinate import *


class TestStringMethods(unittest.TestCase):

    def test_shift(self):
        p1 = Coordinate(0, 1)
        p1.shift(0, -1)
        self.assertEqual(p1, Coordinate(0, 0))

    def test_distance(self):
        pointA = Coordinate(52.2296756, 21.0122287)
        pointB = Coordinate(52.406374, 16.9251681)
        self.assertEqual(distance(pointA, pointB), 278.54558935106695)
        ungs = Coordinate(-34.5359069, -58.7153467)
        pointC = Coordinate(-34.5282916, -58.714135)
        self.assertEqual(distance(ungs, pointC), 0.8542944715822927)


if __name__ == '__main__':
    unittest.main()
