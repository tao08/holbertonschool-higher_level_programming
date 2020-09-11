#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        n_matrix = []
        for colum in matrix:
            n_matrix.append([n ** 2 for n in colum])
        return n_matrix
