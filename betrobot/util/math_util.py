import numpy as np


def sum_submatrix(matrix, indices):
    if len(indices) == 0:
        return 0
    else:
        return matrix[tuple(zip(*indices))].sum()

