import numpy as np


class F2Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.height = len(matrix)
        self.len = len(matrix[0])

    def swap_columns(self, i, j):
        for row in self.matrix:
            row[i], row[j] = row[j], row[i]

    def swap_rows(self, i, j):
        self.matrix[i], self.matrix[j] = self.matrix[j], self.matrix[i]

    def subtract_row(self, from_ind, which_ind):
        zipped = zip(self.matrix[from_ind], self.matrix[which_ind])
        self.matrix[from_ind] = map(lambda x: (x[0] + x[1]) % 2, zipped)

    def transpose(self):
        return F2Matrix(zip(*self.matrix))

    def __str__(self):
        return '\n'.join([str(row) for row in self.matrix])
