from decimal import Decimal, getcontext

from line import MyDecimal
from vector import Vector

getcontext().prec = 30


class Plane(object):
    def __init__(self, normal_vector=None, constant_term=None):
        if not normal_vector:
            all_zeros = ['0'] * 2
            normal_vector = Vector(all_zeros)
        self.normal_vector = Vector([Decimal(x) for x in normal_vector])
        self.dimension = self.normal_vector.dimension

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)
        self.basepoint = None
        self.set_basepoint()

    def set_basepoint(self):
        n = self.normal_vector
        c = self.constant_term
        basepoint_coordinates = ['0'] * self.dimension

        initial_index = Plane.first_nonzero_index(n)
        if initial_index is None:
            self.basepoint = None
        else:
            initial_coefficient = n[initial_index]

            basepoint_coordinates[initial_index] = c / Decimal(initial_coefficient)
            self.basepoint = Vector(basepoint_coordinates)

    def __eq__(self, other):
        """
        Are planes equal?
        :param Plane other: The other plane
        :return Bool: True if planes are equal otherwise false
        """
        are_zero_vectors = self.normal_vector.is_zero_vector() and other.normal_vector.is_zero_vector()
        if are_zero_vectors:
            return self.constant_term == other.constant_term
        return self.normal_vector == other.normal_vector and self.constant_term == other.constant_term

    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            result = ''

            if coefficient < 0:
                result += '-'
            if coefficient > 0 and not is_initial_term:
                result += '+'

            if not is_initial_term:
                result += ' '

            if abs(coefficient) != 1:
                result += '{}'.format(abs(coefficient))

            return result

        n = self.normal_vector

        initial_index = Plane.first_nonzero_index(n)
        if initial_index is None:
            output='0'
        else:
            terms = [write_coefficient(n[i], is_initial_term=(i == initial_index)) + 'x_{}'.format(i + 1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output

    def are_parallel(self, other):
        """
        Are the 2 Planes parallel?
        :param Plane other:
        :return Bool: True if the Planes are parallel
        """
        return self.normal_vector.are_parallel(other.normal_vector)

    def are_equal(self, other):
        """
        Are the 2 Planes equal?
        :param Plane other:
        :return Boolean: True if the Planes are equal
        """
        if not self.are_parallel(other):
            return False
        p1 = self.get_point_on_plane()
        p2 = other.get_point_on_plane()
        vp = Vector([p1[0] - p2[0], p1[1] - p2[1]])
        return vp.are_orthogonal(self.normal_vector) and vp.are_orthogonal(other.normal_vector)

    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        return None

    def get_point_on_plane(self):
        first_nonzero_index = Plane.first_nonzero_index(self.normal_vector)
        if first_nonzero_index is None:
            return 0, 0, 0

        result = []
        for k, item in enumerate(self.normal_vector):
            if k == first_nonzero_index:
                result.append(self.constant_term / item)
            else:
                result.append(0)

        return tuple(result)

