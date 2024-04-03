#!/usr/bin/python3
"""
A module "Square".

This module contains a simple Square class with initialized size.
Size defaults to 0. Raise errors on invalid inputs.
"""


class Square:
    """A class that defines a Square by size"""
    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
