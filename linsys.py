from decimal import getcontext

from copy import deepcopy

from line import MyDecimal
from plane import Plane

getcontext().prec = 30



class LinearSystem(object):
    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def swap_rows(self, row1, row2):
        tmp = self.planes[row1]
        self.planes[row1] = self.planes[row2]
        self.planes[row2] = tmp

    def multiply_coefficient_and_row(self, coefficient, row):
        self.planes[row] = Plane(self.planes[row].normal_vector * coefficient,
                                 self.planes[row].constant_term * coefficient)

    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        p = Plane(self.planes[row_to_add].normal_vector, self.planes[row_to_add].constant_term)
        p.normal_vector = p.normal_vector * coefficient
        p.constant_term *= coefficient
        self.planes[row_to_be_added_to] = Plane(
            self.planes[row_to_be_added_to].normal_vector + p.normal_vector,
            self.planes[row_to_be_added_to].constant_term + p.constant_term)

    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)

        indices = [-1] * num_equations

        for i, p in enumerate(self.planes):
            indices[i] = p.first_nonzero_index(p.normal_vector)

        return indices

    def __len__(self):
        return len(self.planes)

    def __getitem__(self, i):
        return self.planes[i]

    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i + 1, p) for i, p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret

    def compute_triangular_form(self):
        system = deepcopy(self)
        num_equations = len(system)
        num_variables = system.dimension

        j = 0
        for i in range(num_equations):
            while j < num_variables:
                c = MyDecimal(system[i].normal_vector[j])
                if c.is_near_zero():
                    swap_succeeded = system.swap_with_row_below_for_nonzero_coef(i, j)
                    if not swap_succeeded:
                        j += 1
                        continue
                system.clear_coefficients_below(i, j)
                i += 1
                break
        return system

    def swap_with_row_below_for_nonzero_coef(self, row, column):
        num_equations = len(self)

        for k in range(row + 1, num_equations):
            coef = MyDecimal(self[k].normal_vector[column])
            if not coef.is_near_zero():
                self.swap_rows(row, k)
                return True
        return False

    def clear_coefficients_below(self, row, column):
        num_equations = len(self)
        beta = MyDecimal(self[row].normal_vector[column])
        for k in range(row + 1, num_equations):
            n = self[k].normal_vector
            gamma = n[column]
            alpha = -gamma/beta
            self.add_multiple_times_row_to_row(alpha, row, k)
