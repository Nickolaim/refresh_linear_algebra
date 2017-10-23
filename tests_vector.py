#!/usr/bin/env python

import unittest

from vector import Vector


class VectorTestCase(unittest.TestCase):
    def test_addition(self):
        v1 = Vector([0, 0, 0])
        v2 = Vector([1, 1, 1])
        self.assertEqual(v2, v1+v2)

    def test_substaction(self):
        self.assertEqual(Vector([-1, -1]), Vector([0, 0]) - Vector([1,1]))

    def test_quiz(self):
        v1 = Vector([8.218, -9.341])
        v2 = Vector([-1.129, 2.111])
        v3 = v1 + v2
        print(v3)

        v4 = Vector([7.119, 8.215])
        v5 = Vector([-8.223, 0.878])
        v6 = v4 - v5
        print(v6)

if __name__ == '__main__':
    unittest.main()
