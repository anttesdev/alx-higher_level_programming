#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    if matrix:
        cols = len(matrix[0])
    else:
        cols = 0
    square = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            square[i][j] = matrix[i][j] ** 2
    return square
