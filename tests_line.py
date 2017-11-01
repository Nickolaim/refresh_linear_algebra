import unittest

from line import Line
from vector import Vector


class LineTestCase(unittest.TestCase):
    def test_is_parallel(self):
        self.assertTrue(Line(Vector([3, -2]), 1).is_parallel(Line(Vector([-6, 4]))))


if __name__ == '__main__':
    unittest.main()
