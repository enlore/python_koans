#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    # sane sides check:
    # the sum of any two sides must be greater than the third
    def checker(op, op1, side):
        if op + op1 <= side:
            raise TriangleError

    for op, op1, side in [
            (a, b, c), (a, c, b), 
            (b, c, a), (b, a, c), 
            (c, a, b), (c, b, a)]:
        checker(op, op1, side)

    if a < 1 or b < 1 or c < 1:
        raise TriangleError

    if a == b == c and a != 0:
        return 'equilateral'

    if a == b or a == c or b == c:
        return 'isosceles'

    if a != b and a != c and b != c:
        return 'scalene'

    raise TriangleError

# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
