import unittest

from plane import Plane
from vector import Vector


class PlaneTestCase(unittest.TestCase):
    def test_are_equal(self):
        self.assertTrue(
            Plane(Vector([-0.412, 3.806, 0.728]), -3.46).are_equal(Plane(Vector([1.03, -9.515, -1.82]), 8.65)))
        self.assertFalse(
            Plane(Vector([2.611, 5.528, 0.283]), 4.6).are_equal(Plane(Vector([7.715, 8.306, 5.342]), 3.76)))

    def test_are_parallel(self):
        self.assertTrue(
            Plane(Vector([-0.412, 3.806, 0.728]), -3.46).are_parallel(Plane(Vector([1.03, -9.515, -1.82]), 8.65)))
        self.assertFalse(
            Plane(Vector([2.611, 5.528, 0.283]), 4.6).are_parallel(Plane(Vector([7.715, 8.306, 5.342]), 3.76)))


if __name__ == '__main__':
    unittest.main()
