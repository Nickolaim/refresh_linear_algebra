#!/usr/bin/env python

import math
import unittest

from vector import Vector


class VectorTestCase(unittest.TestCase):
    def test_addition(self):
        v1 = Vector([0, 0, 0])
        v2 = Vector([1, 1, 1])
        self.assertEqual(v2, v1 + v2)

    def test_subtraction(self):
        self.assertEqual(Vector([-1, -1]), Vector([0, 0]) - Vector([1, 1]))

    def test_multiplication(self):
        self.assertEqual(Vector([2, -2]), Vector([1, -1]) * 2)

    def test_magnitude(self):
        self.assertEqual(5, Vector([4, 3]).magnitude())

    def test_normalize(self):
        self.assertEqual(Vector([1 / math.sqrt(2), 1 / math.sqrt(2)]), Vector([2, 2]).normalized_vector())

    def test_dot_product(self):
        self.assertEqual(4, Vector([1, 1]).dot_product(Vector([2, 2])))

    def test_angle(self):
        self.assertAlmostEqual(math.pi / 2, Vector([0, 1]).angle(Vector([1, 0])))
        self.assertAlmostEqual(0, Vector([1, 1]).angle(Vector([1, 1]), "degree"), places = 5)

    def test_quiz(self):
        print(Vector([7.887, 4.138]).dot_product(Vector([-8.802, 6.776])))
        print(Vector([-5.955, -4.904, -1.874]).dot_product(Vector([-4.496, -8.755, 7.103])))
        print(Vector([3.183, -7.627]).angle(Vector([-2.668, 5.319])))
        print(Vector([7.35, 0.221, 5.188]).angle(Vector([2.751, 8.259, 3.985]), "degree"))


if __name__ == '__main__':
    unittest.main()
