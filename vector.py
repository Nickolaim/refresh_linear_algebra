#!/usr/bin/env python


import numbers
from math import sqrt, acos, pi

from decimal import Decimal

TOLERANCE = 1e-10


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(a) for a in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __iter__(self):
        return iter(self.coordinates)

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __getitem__(self, index):
        return self.coordinates[index]

    def __eq__(self, other):
        if len(self.coordinates) != len(other.coordinates):
            return False
        for x,y in zip(self.coordinates, other.coordinates):
            if abs(x - y) > TOLERANCE:
                return False
        return True

    def __add__(self, other):
        assert other.dimension == self.dimension
        result = [x + y for x, y in zip(self.coordinates, other.coordinates)]
        return Vector(result)

    def __sub__(self, other):
        assert other.dimension == self.dimension
        result = [x - y for x, y in zip(self.coordinates, other.coordinates)]
        return Vector(result)

    def __mul__(self, scalar):
        """
        Multiply vector by a scalar
        :param Number scalar: scalar for multiplication
        :return Vector: multiplied vector
        """
        assert isinstance(scalar, numbers.Number)
        result = [x * scalar for x in self.coordinates]
        return Vector(result)

    def magnitude(self):
        return Decimal(sqrt(sum([i * i for i in self.coordinates])))

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
        angle_with_potential_precision_problem = self.dot_product(other) / (self.magnitude() * other.magnitude())
        if -1.0 > angle_with_potential_precision_problem > -1.0 - TOLERANCE:
            angle_with_potential_precision_problem = -1.0
        elif 1 < angle_with_potential_precision_problem < 1 + TOLERANCE:
            angle_with_potential_precision_problem = 1.0
        angle_rad = acos(angle_with_potential_precision_problem)
        return angle_rad if degree_or_radian == "radian" else angle_rad * 180.0 / pi

    def is_zero_vector(self):
        set_coordinates = set(self.coordinates)
        return len(set_coordinates) == 1 and 0 in set_coordinates

    def are_parallel(self, other, tolerance=TOLERANCE):
        if self.is_zero_vector() or other.is_zero_vector():
            return True
        angle = self.angle(other)
        return abs(angle) < tolerance or abs(angle - pi) < tolerance

    def are_orthogonal(self, other, tolerance=TOLERANCE):
        return abs(self.dot_product(other)) < tolerance

    def projection(self, other):
        """
        Project the other vector to self
        :param Vector other: other vector
        :return Vector: projection of the other vector to this vector
        """
        c = self.dot_product(other) / self.dot_product(self)
        return self * c

    def cross_product(self, other):
        """
        Cross product of self and the other vector
        :param Vector other: the other vector
        :return Vector: cross product vector
        """
        return Vector([
            self.coordinates[1] * other.coordinates[2] - other.coordinates[1] * self.coordinates[2],
            -(self.coordinates[0] * other.coordinates[2] - other.coordinates[0] * self.coordinates[2]),
            self.coordinates[0] * other.coordinates[1] - other.coordinates[0] * self.coordinates[1]
        ])
