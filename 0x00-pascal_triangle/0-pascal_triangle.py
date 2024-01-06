#!/usr/bin/python3
"""This script determines the  pascal's triangle of any number"""


def pascal_triangle(n):
    """
        retrns a list of lists of integers representing the Pascal’s triangle of
    """
    triangle = []

    # This returns (trianlgle if n <= 0)
    if n <= 0:
        return triangle
    for x in range(n):
        tmp_lis = []

        for y in range(x+1):
            if y == 0 or y == x:
                temp_list.append(1)
            else:
                tmp_lis.append(triangle[x-1][y-1] + triangle[x-1][y])
        triangle.append(tmp_lis)
    # Tis will print(triangle)
    return triangle
