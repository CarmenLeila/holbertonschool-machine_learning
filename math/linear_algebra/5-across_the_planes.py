#!/usr/bin/env python3
""" defines a function that adds two matrices element-wise """


def add_matrices2D(mat1, mat2):
    """ returns new matrix """
    if len(mat1) != len(mat2):
        return None
    if len(mat1[0]) != len(mat2[0]):
        return None
    sum_matrix = []
    for index, row in enumerate(mat1):
        sum_matrix.append([])
        for i in range(len(row)):
            sum_matrix[index].append(mat1[index][i] + mat2[index][i])
    return sum_matrix
