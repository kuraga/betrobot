import numpy as np


def sum_submatrix(matrix, indices):
    if len(indices) == 0:
        return 0
    else:
        return matrix[tuple(zip(*indices))].sum()


def get_weights_array(size, weights=None):
    if weights is None:
        weights = np.ones((size,)) / size
    else:
        weights = np.array(weights)

    result = np.zeros((size,))
    t = np.min([weights.size, size])
    result[-t:] = weights[-1:(-t-1):-1]

    return result
