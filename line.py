from decimal import Decimal, getcontext

from vector import Vector

getcontext().prec = 30


class Line(object):
    NO_NONZERO_ELEMENTS_FOUND = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = ['0'] * self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = Vector([Decimal(x) for x in normal_vector])

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)
        self.basepoint = None
        self.set_basepoint()

    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coordinates = ['0'] * self.dimension

            initial_index = Line.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coordinates[initial_index] = c / Decimal(initial_coefficient)
            self.basepoint = Vector(basepoint_coordinates)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELEMENTS_FOUND:
                self.basepoint = None
            else:
                raise e

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

        try:
            initial_index = Line.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i == initial_index)) + 'x_{}'.format(i + 1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELEMENTS_FOUND:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output

    def are_parallel(self, other):
        """
        Are the 2 lines parallel?
        :param Line other:
        :return Bool: True if the lines are parallel
        """
        return self.normal_vector.are_parallel(other.normal_vector)

    def are_equal(self, other):
        """
        Are the 2 lines equal?
        :param Line other:
        :return Boolean: True if the lines are equal
        """
        if not self.are_parallel(other):
            return False
        p1 = self.get_point_on_line()
        p2 = other.get_point_on_line()
        vp = Vector([p1[0] - p2[0], p1[1] - p2[1]])
        return vp.are_orthogonal(self.normal_vector) and vp.are_orthogonal(other.normal_vector)

    def intersection(self, other):
        """
        What is intersection point of 2 lines?
        :param Line other: Line that is intersected with
        :return (float, float):  Intersection point if exists, otherwise None
        """
        if self.are_parallel(other):
            return None

        den = self.normal_vector[0] * other.normal_vector[1] - self.normal_vector[1] * other.normal_vector[0]
        x = (other.normal_vector[1] * self.constant_term - self.normal_vector[1] * other.constant_term) / den
        y = (-other.normal_vector[0] * self.constant_term + self.normal_vector[0] * other.constant_term) / den
        return x, y

    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Line.NO_NONZERO_ELEMENTS_FOUND)

    def get_point_on_line(self):
        if self.normal_vector[0] == self.normal_vector[1] == 0:
            return 0, 0
        if self.normal_vector[0] == 0:
            return 0, self.constant_term / self.normal_vector[1]

        return self.constant_term / self.normal_vector[0], 0


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
