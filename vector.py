#!/usr/bin/env python


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
        result = []
        for i in range(0, self.dimension):
            result.append(self.coordinates[i] + other.coordinates[i])
        return Vector(result)

    def __sub__(self, other):
        assert other.dimension == self.dimension
        result = []
        for i in range(0, self.dimension):
            result.append(self.coordinates[i] - other.coordinates[i])
        return Vector(result)