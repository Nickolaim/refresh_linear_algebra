#!/usr/bin/env python

import unittest
import math
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
        self.assertEqual(Vector([1/math.sqrt(2), 1/math.sqrt(2)]), Vector([2, 2]).normalized_vector())

    def test_quiz(self):
        v1 = Vector([8.218, -9.341])
        v2 = Vector([-1.129, 2.111])
        v3 = v1 + v2
        print(v3)

        v4 = Vector([7.119, 8.215])
        v5 = Vector([-8.223, 0.878])
        v6 = v4 - v5
        print(v6)

        v7 = Vector([1.671, -1.012, -0.318]) * 7.41
        print(v7)

        print(Vector([-0.221, 7.437]).magnitude())
        print(Vector([8.813, -1.331, -6.247]).magnitude())
        print(Vector([5.581, -2.136]).normalized_vector())
        print(Vector([1.996, 3.108, -4.554]).normalized_vector())


if __name__ == '__main__':
    unittest.main()
