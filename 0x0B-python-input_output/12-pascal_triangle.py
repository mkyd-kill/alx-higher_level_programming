#!/usr/bin/python3
"""
Returns a list of integers representing the Pascal
Triangle of n
"""


def pascal_triangle(n: int):
    """Pascal triangle list results"""
    result = [[1]]

    if n <= 0:
        return []
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(result[i - 1][j - 1] + result[i - 1][j])
        row.append(1)
        result.append(row)
    return result
