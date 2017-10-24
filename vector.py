#!/usr/bin/env python


import numbers
from math import sqrt, acos, pi


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def __add__(self, other):
        assert other.dimension == self.dimension
        result = [x + y for x, y in zip(self.coordinates, other.coordinates)]
        return Vector(result)

    def __sub__(self, other):
        assert other.dimension == self.dimension
        result = [x - y for x, y in zip(self.coordinates, other.coordinates)]
        return Vector(result)

    def __mul__(self, other):
        assert isinstance(other, numbers.Number)
        result = [x * other for x in self.coordinates]
        return Vector(result)

    def magnitude(self):
        return sqrt(sum([i * i for i in self.coordinates]))

    def normalized_vector(self):
        try:
            magnitude = self.magnitude()
            result = [x / magnitude for x in self.coordinates]
            return Vector(result)
        except ZeroDivisionError:
            raise Exception("Cannot normalize zero vector")

    def dot_product(self, other):
        return sum([x * y for x, y in zip(self.coordinates, other.coordinates)])

    def angle(self, other, degree_or_radian="radian"):
        angle_rad = acos(self.dot_product(other) / (self.magnitude() * other.magnitude()))
        return angle_rad if degree_or_radian == "radian" else angle_rad * 180.0 / pi
