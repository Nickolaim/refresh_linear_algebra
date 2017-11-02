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

    def test_quiz(self):
        lines = [
            (Line(Vector([4.046, 2.836]), 1.21),
             Line(Vector([10.115, 7.09]), 3.025)),
            (Line(Vector([7.204, 3.182]), 8.68),
             Line(Vector([8.172, 4.114]), 9.883)),
            (Line(Vector([1.182, 5.562]), 6.744),
             Line(Vector([1.773, 8.343]), 9.525)),
        ]
        for l1, l2 in lines:
            print("Intersection: {}".format(l2.intersection(l1)))
            print("Is same line: {}".format(l2.are_equal(l1)))


if __name__ == '__main__':
    unittest.main()
