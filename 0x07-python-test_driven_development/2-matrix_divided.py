#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    A function that divides everly element of a matrix
    by a number
    Args:
        matrix(list): a list of list of numbers or floats
        div(int or float): the divider number
    Return: A matrix of the numbers divided
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(error)
    for child_list in matrix:
        if not isinstance(child_list, list):
            raise TypeError(error)
        if len(child_list) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for num in child_list:
            if not isinstance(num, (int, float)):
                raise TypeError(error)
    new_matrix = [
        [round(num / div, 2) for num in child_list]
        for child_list in matrix
        ]
    return new_matrix
