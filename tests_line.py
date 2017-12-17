import unittest

from line import Line
from vector import Vector


class LineTestCase(unittest.TestCase):
    def test_are_parallel(self):
        self.assertTrue(Line(Vector([3, -2]), 1).are_parallel(Line(Vector([-6, 4]))))
        self.assertFalse(Line(Vector([1, 2]), 3).are_parallel(Line(Vector([1, -1]), 2)))

    def test_are_equal(self):
        self.assertTrue(Line(Vector([1, 1]), 1).are_equal(Line(Vector([3, 3]), 3)))
        self.assertFalse(Line(Vector([1, 1]), 1).are_equal(Line(Vector([3, 3]), 1)))

    def test_intersection(self):
        intersection = Line(Vector([0, 1])).intersection(Line(Vector([5, 0])))
        self.assertAlmostEquals(0, intersection[0])
        self.assertAlmostEquals(0, intersection[1])


if __name__ == '__main__':
    unittest.main()
