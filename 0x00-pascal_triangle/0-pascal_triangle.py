#!/usr/bin/python3
"""
Pascals Triangle
"""


def pascal_triangle(n):
    """
    Function that returns a list of binomial
    coefficients representing the Pascals
    triangle of n
    """
    if n <= 0:
        return []
    p_triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(p_triangle[i - 1][j - 1] + ,p_triangle[i - 1][j])
        row.append(1)
        p_triangle.append(row)
    return p_triangle
