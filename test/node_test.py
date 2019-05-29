import unittest

from src.node import *


class TestStringMethods(unittest.TestCase):

    def test_shift(self):
        n1 = Node(0, 1, 10)
        n1.shift(0, -1)
        self.assertEqual(n1.get_center(), Point(0, 0))

    def test_shift_radius(self):
        n1 = Node(0, 1, 10)
        n2 = Node(0, 1, 10)
        n1.shift_radius(10)
        n2.shift_radius(-20)
        self.assertEqual(n1.radius, 20)
        self.assertEqual(n2.radius, -10)

    def test_in_radius(self):
        n1 = Node(0, 0, 10)
        p1 = Point(1, 1)
        p2 = Point(10, 10)
        self.assertTrue(n1.in_radius(p1))
        self.assertFalse(n1.in_radius(p2))

    def test_point_distance_to_center(self):
        n1 = Node(0, 8, 10)
        p1 = Point(3, 4)
        self.assertEqual(n1.point_distance_to_center(p1), 5)

    def test_node_distance_to_center(self):
        n1 = Node(0, 0, 1)
        n2 = Node(1.5, 0, 1)
        self.assertEqual(n1.node_distance_to_center(n2), 0.5)

    def test_within_range(self):
        n1 = Node(0, 0, 1)
        n2 = Node(2.1, 0, 1)
        n3 = Node(2, 0, 1)
        n4 = Node(0, 0, 1)
        self.assertFalse(within_range(n1, n2))
        self.assertTrue(within_range(n1, n3))
        self.assertTrue(n1, n4)


if __name__ == '__main__':
    unittest.main()
