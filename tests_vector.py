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
        self.assertAlmostEqual(0, Vector([1, 1]).angle(Vector([1, 1]), "degree"), places=5)

    def test_is_parallel(self):
        self.assertTrue(Vector([1, 2, 3]).is_parallel(Vector([2, 4, 6])))
        self.assertFalse(Vector([3, 1]).is_parallel(Vector([1, 1])))
        self.assertTrue(Vector([3, 1]).is_parallel(Vector([0, 0])))

    def test_is_orthogonal(self):
        self.assertFalse(Vector([1, 2, 3]).is_orthogonal(Vector([2, 4, 6])))
        self.assertTrue(Vector([1, 0]).is_orthogonal(Vector([0, 5])))

    def test_projection(self):
        self.assertEqual(Vector([1, 1]), Vector([1, 1]).projection(Vector([1, 1])))
        self.assertEqual(Vector([0, 0]), Vector([1, 0]).projection(Vector([0, 1])))

    def test_cross_product(self):
        self.assertAlmostEquals(Vector([9, -13, 3]), Vector([5, 3, -2]).cross_product(Vector([-1, 0, 3])))

    def test_quiz(self):
        test = [
            (Vector([-7.579, -7.88]), Vector([22.737, 23.64])),
            (Vector([-2.029, 9.97, 4.172]), Vector([-9.231, -6.639, -7.245])),
            (Vector([-2.328, -7.284, -1.214]), Vector([-1.821, 1.072, -2.94])),
            (Vector([2.118, 4.827]), Vector([0, 0])),
        ]
        for t in test:
            print(t[0].is_parallel(t[1]))
            print(t[0].is_orthogonal(t[1]))

        print(Vector([8.462, 7.893, -8.187]).cross_product(Vector([6.984, -5.975, 4.778])))
        v1 = Vector([-8.987, -9.838, 5.031]).cross_product(Vector([-4.268, -1.861, -8.866]))
        print(v1.magnitude())
        v2 = Vector([1.5, 9.547, 3.691]).cross_product(Vector([-6.007, 0.124, 5.772]))
        print (v2.magnitude() / 2)

if __name__ == '__main__':
    unittest.main()
