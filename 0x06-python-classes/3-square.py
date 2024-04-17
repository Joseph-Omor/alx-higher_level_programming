#!/usr/bin/python3
"""
This is the "Square" module.

This module provides a simple Square class ...
"""


class Square:
    """A class that can compute the area of a square defined by size"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
