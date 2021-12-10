#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    a function to divide all elements of a matrix by div parameter
    """
    new_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        inner_list = []
        for items in lists:
            if not isinstance(items, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            else:
                inner_list.append(round(items / div, 2))
        new_matrix.append(inner_list)
    return new_matrix
