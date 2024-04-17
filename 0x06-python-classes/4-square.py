#!/usr/bin/python3
"""
The "Square" module.

It provides a simple Square class with initialize size.
Defaults size to 0. Raises error on invalide size inputs.
Methods Getter and Setter properties for size.
Method area returns size of area of the sqare.
"""


class Square:
    """A class that can compute the area of a square defined by size"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
