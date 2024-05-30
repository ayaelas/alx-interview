#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """returns a list of lists of int representing the Pascal’s triangle of n
    """
    end = []
    if n > 0:
        for i in range(1, n + 1):
            xide = []
            k = 1
            for j in range(1, i + 1):
                xide.append(k)
                k = k * (i - j) // j
            end.append(xide)
    return end
